# Generated by Django 3.0.6 on 2020-06-02 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200602_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 14, 25, 46, 274253, tzinfo=utc)),
        ),
    ]