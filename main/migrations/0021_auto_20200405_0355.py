# Generated by Django 2.1.5 on 2020-04-04 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200405_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='tutorial_slug',
            field=models.CharField(default='series', max_length=200),
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 3, 55, 56, 470323), verbose_name='date published'),
        ),
    ]
