from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ItemsForm, Cats, SignUp
from django.contrib.auth.models import User
from .models import Items, Cats
from django.views.generic.edit import FormView


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
    sales_goods = Items.objects.filter(on_sale=True)
    goods = Items.objects.all()
    print(Items.objects.get(id=1).on_sale, Items.objects.get(id=1).name, Items.objects.get(id=1).previous_price)
    return render(request, 'base.html',
                  {"goods": goods, 'sales_goods': sales_goods, 'cats_nav': None})


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
