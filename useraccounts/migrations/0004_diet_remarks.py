# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-01 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0003_diet_ts'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='remarks',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]