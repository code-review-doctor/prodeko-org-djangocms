# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_vaalit', '0010_auto_20180603_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kysymys',
            old_name='to_applicant',
            new_name='to_virka',
        ),
    ]
