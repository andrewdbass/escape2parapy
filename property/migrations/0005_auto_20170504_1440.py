# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20170504_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unavailabledate',
            name='prop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unavailable_dates', to='property.Property'),
        ),
    ]
