# Generated by Django 2.1.5 on 2020-04-10 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200411_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 3, 31, 24, 421968), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 3, 31, 24, 391966), verbose_name='date published'),
        ),
    ]