# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20180508_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenq',
            name='imagenQ',
            field=models.ImageField(default='static/media/', upload_to='static/'),
        ),
    ]
