# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180415_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosttournament',
            name='player_list',
        ),
        migrations.AddField(
            model_name='hosttournament',
            name='player_rsvp',
            field=models.IntegerField(null=True),
        ),
    ]