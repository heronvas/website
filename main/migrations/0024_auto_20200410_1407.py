# Generated by Django 2.1.5 on 2020-04-10 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200405_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='series_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 7, 23, 886663), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 7, 23, 912665), verbose_name='date published'),
        ),
    ]
