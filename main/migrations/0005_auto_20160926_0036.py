# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160925_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
