# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-07-11 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0016_auto_20200711_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slamchart',
            name='response',
            field=models.BooleanField(default=True),
        ),
    ]
