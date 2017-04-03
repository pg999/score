# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0008_auto_20161007_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=1000)),
                ('budget', models.IntegerField()),
                ('loc', models.CharField(max_length=100)),
                ('s_time', models.DateTimeField(max_length=50)),
                ('e_time', models.DateTimeField(max_length=50)),
                ('about', models.CharField(max_length=500)),
                ('v_admin', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
