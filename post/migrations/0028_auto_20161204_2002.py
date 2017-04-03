# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20161204_2002'),
        ('post', '0027_auto_20161204_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='passbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=7)),
                ('r_id', models.CharField(max_length=7)),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AlterField(
            model_name='post_response',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
