# Generated by Django 2.1.5 on 2020-04-04 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200403_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 13, 22, 13, 960980), verbose_name='date published'),
        ),
    ]
