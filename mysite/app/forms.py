from django.forms import ModelForm
from django.forms import forms, CharField, TextInput
from .models import Items, Marks, Cats
from django.contrib.auth.models import User


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'marks', 'category', 'picture', 'article_number', 'price', 'previous_price']


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = ['name', 'location']


class SignUp(forms.Form):
    username = CharField(label='username', max_length=150,
                         widget=TextInput(attrs={'required': True, "class": 'input', 'type': "text"}))
    email = CharField(label='Username', max_length=150,
                      widget=TextInput(attrs={'required': True, "class": 'input', 'type': "text"}))
    password = CharField(label='Password', max_length=150,
                         widget=TextInput(attrs={'required': True, "class": 'input', 'type': "password"}))
    repeat_password = CharField(label='Repeat your password', max_length=150,
                                widget=TextInput(attrs={'required': True, "class": 'input', 'type': "password"}))
