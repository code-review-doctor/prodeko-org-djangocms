# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 20:20
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifelonglearning', '0002_auto_20180823_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.AddField(
            model_name='course',
            name='open',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='timing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='coaches',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='groupsize',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
