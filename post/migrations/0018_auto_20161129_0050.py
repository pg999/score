# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20161126_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_response',
            old_name='budget_max',
            new_name='bid',
        ),
        migrations.RemoveField(
            model_name='post_response',
            name='budget_min',
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AlterField(
            model_name='post_response',
            name='post_id',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='post_response',
            name='user_id',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
