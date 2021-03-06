# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-03 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccounts', '0008_auto_20180203_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='credittable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('messname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.messcanteen')),
            ],
        ),
        migrations.RemoveField(
            model_name='diet',
            name='credit',
        ),
    ]
