# Generated by Django 3.0.6 on 2020-06-05 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200604_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 5, 8, 4, 55, 253571, tzinfo=utc)),
        ),
    ]
