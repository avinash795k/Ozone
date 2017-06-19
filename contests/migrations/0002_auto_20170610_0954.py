# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-10 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='setter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
