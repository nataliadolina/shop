# Generated by Django 3.0.6 on 2020-06-02 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200601_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cats'),
        ),
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 13, 2, 35, 846496, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='marks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Marks'),
        ),
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='previous_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='video',
            field=models.TextField(null=True),
        ),
    ]
