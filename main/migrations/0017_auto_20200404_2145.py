# Generated by Django 2.1.5 on 2020-04-04 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200404_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 21, 45, 44, 829972), verbose_name='date published'),
        ),
    ]