# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Textbooks', '0006_auto_20181024_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='edition',
        ),
    ]
