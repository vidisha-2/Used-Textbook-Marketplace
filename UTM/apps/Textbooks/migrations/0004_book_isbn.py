# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-23 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Textbooks', '0003_auto_20181023_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.BigIntegerField(default=0),
        ),
    ]
