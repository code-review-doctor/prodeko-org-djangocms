# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kulukorvaus', '0007_auto_20180518_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kulukorvaus',
            name='explanation',
            field=models.CharField(max_length=100, verbose_name='Tapahtuma / kulun kohde'),
        ),
    ]
