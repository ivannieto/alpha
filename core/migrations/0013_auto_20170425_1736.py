# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170425_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='postal_code',
            field=models.TextField(blank=True, default='', verbose_name='Código postal'),
        ),
    ]