# Generated by Django 2.1.5 on 2020-05-04 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='series_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 3, 6, 28, 302463), verbose_name='date published'),
        ),
    ]