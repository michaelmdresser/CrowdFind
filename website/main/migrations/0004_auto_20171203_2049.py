# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171203_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='latitude',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='longitude',
            field=models.TextField(default=0),
        ),
    ]
