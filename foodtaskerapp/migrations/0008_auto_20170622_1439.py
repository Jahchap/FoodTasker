# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0007_auto_20170622_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Driver'),
        ),
    ]
