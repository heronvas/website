# Generated by Django 2.1.5 on 2020-04-03 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200403_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='series_slug',
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 14, 48, 39, 439306), verbose_name='date published'),
        ),
    ]
