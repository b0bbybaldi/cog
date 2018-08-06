# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 06:24
from __future__ import unicode_literals

import app.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cog',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, storage=app.storage.MinioCogStorage(), upload_to=''),
        ),
    ]