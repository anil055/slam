# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-06-20 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0002_auto_20200619_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactertemplate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
