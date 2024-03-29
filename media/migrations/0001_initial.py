# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-21 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('media', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_poster', models.CharField(max_length=25)),
                ('reaction_title', models.CharField(max_length=50)),
                ('reaction_description', models.CharField(max_length=5000)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Picture')),
            ],
        ),
    ]
