# Generated by Django 2.1.5 on 2020-04-11 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200411_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 14, 29, 38, 186863), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 14, 29, 38, 153861), verbose_name='date published'),
        ),
    ]