# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20170921_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_desc',
            field=models.CharField(default='', max_length=250),
        ),
    ]
