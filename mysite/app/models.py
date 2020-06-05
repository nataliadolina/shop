from django.db import models
from django.db.models import AutoField, DateField, CharField, ForeignKey, DecimalField, TextField, EmailField, BooleanField
from django.utils import timezone
from django.urls import reverse


class Marks(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return '%s' % self.name


class Cats(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=150)
    LOC_CHOICES = [('nav', 'navigation panel'), ('main', 'mainpage'), ('footer', 'Footer'), ("side_menu", 'side_menu')]
    location = CharField(max_length=150, choices=LOC_CHOICES, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return '%s' % self.name

    def get_category_url(self):
        return reverse('items_with_specific_cat', kwargs={'name': self.name})


class Items(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=150)
    date = DateField(default=timezone.now())
    marks = ForeignKey(Marks, on_delete=models.DO_NOTHING, null=True)
    category = ForeignKey(Cats, on_delete=models.DO_NOTHING, null=True)
    price = DecimalField(max_digits=7, decimal_places=2)
    previous_price = DecimalField(max_digits=7, decimal_places=2, null=True)
    on_sale = BooleanField(default=False)
    article_number = CharField(max_length=150)
    description = TextField(null=True)
    picture = TextField(null=True)
    video = TextField(null=True)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('item', kwargs={'id': self.id})
