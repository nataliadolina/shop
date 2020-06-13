from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ItemsForm, Cats, SignUp, LoadExcelFile
from django.contrib.auth.models import User
from .models import Items, Cats, Marks
from django.views.generic.edit import FormView
import win32com.client
import openpyxl
from io import BytesIO
import numpy as np


def index(request):
    context = {'cats_nav': Cats.objects.filter(location='nav'), 'objects': Items.objects.all()}
    return render(request, 'index.html', context)


def add_item(request, id):
    if id == 0:
        form = ItemsForm
    else:
        instance = Items.objects.get(id=id)
        form = ItemsForm(instance)
    context = {'form': form}
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        inf = form.save(commit=False)
        data = inf.picture
        inf.picture = 'http://drive.google.com/uc?export=view&id=' + data
        if inf.previous_price:
            inf.on_sale = True
    return render(request, 'add_item.html', context)


def add_user(request):
    form = SignUp()
    if request.method == "POST":
        form = SignUp(request.POST)
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        username = form.cleaned_data['username']
        if password != repeat_password:
            form.cleaned_data['repeat_password'] = ''
            return render(request, 'register.html', {"form": form})
    return render(request, 'register.html', {"form": form})


def home(request):
    # make array to make a neat layout in template
    sales_goods = list(Items.objects.filter(on_sale=True))
    print(sales_goods)
    indexes, length = return_divisible_list(3, sales_goods)
    sales_goods_indexes = np.array(indexes).reshape((length // 3, 3))

    goods = list(Items.objects.all())
    indexes, length = return_divisible_list(3, goods)
    goods_indexes = np.array(indexes).reshape((length // 3, 3))
    return render(request, 'index.html',
                  {"goods": goods, 'sales_goods': sales_goods, "sales_goods_indexes": sales_goods_indexes,
                   "goods_indexes": goods_indexes})


def return_divisible_length(number, query):
    length = len(query)
    if length % number == 0:
        return length, length
    return length // number + number, length


def return_divisible_list(number, query):
    query_length = len(query)
    result = list(query) + (number - query_length % number) * [-1]
    return result, len(result)


def all_items(request, name):
    goods = Items.objects.filter(category=Cats.objects.filter(name=name))
    sales_goods = Items.objects.filter(category=Cats.objects.filter(name=name), on_sale=True)
    return render(request, 'all_items.html',
                  {"goods": goods, 'sales_goods': sales_goods, 'cats_nav': Cats.objects.filter(location='nav')})


def item(request, id):
    item = Items.objects.filter(id=id)
    return render(request, 'index.html', {"item": item})


def example(request):
    return render(request, 'simple_example/index.html')


def get_excel_file(request):
    form = LoadExcelFile()
    if request.method == 'POST':
        form = LoadExcelFile(request.POST)
        file = request.FILES['file']

        wb = openpyxl.load_workbook(filename=BytesIO(file.read()))
        sheet = wb['Лист1']
        row = 2
        name = sheet['A{0}:I{0}'.format(row)][0][0]
        while name.value:
            name, mark, category, price, previous_price, article_number, description, picture, video = \
                sheet['A{0}:I{0}'.format(row)][0]
            row += 1
            if previous_price.value:
                on_sale = True
            else:
                on_sale = False
            marks, cat = None, None
            if mark.value:
                marks = Marks(name=mark.value)
                marks.save()
            if category.value:
                cat = Cats(name=category.value)
                cat.save()
            if name.value:
                item = Items(name=name.value, marks=marks, category=cat, price=price.value,
                             previous_price=previous_price.value, on_sale=on_sale,
                             article_number=str(article_number.value), description=description.value,
                             picture=picture.value, video=video.value)
                item.save()
                row += 1
            else:
                break
    return render(request, 'uploadform.html', {"form": form})
