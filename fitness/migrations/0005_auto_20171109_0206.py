# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_auto_20171109_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexercise',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Exercise'),
        ),
    ]