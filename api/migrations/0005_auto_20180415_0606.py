# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180415_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourite_game',
        ),
        migrations.AlterField(
            model_name='user',
            name='fav_game',
            field=models.CharField(max_length=50, null=True),
        ),
    ]