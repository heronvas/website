# Generated by Django 2.1.5 on 2020-03-31 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200330_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='file',
            field=models.FileField(default='DEFAULT VALUE', max_length=140, upload_to=''),
        ),
        migrations.AlterField(
            model_name='disco',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 2, 36, 43, 318320), verbose_name='date published'),
        ),
    ]