# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-07-11 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0012_answer_mess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='binary',
        ),
    ]
