# Generated by Django 2.1.5 on 2020-04-05 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200405_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disco',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 19, 53, 54, 395288), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='disco',
            name='title',
            field=models.CharField(default='1', max_length=200),
        ),
    ]