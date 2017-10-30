# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('completed_sets', models.IntegerField()),
                ('max_sets', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Exercise')),
            ],
        ),
    ]
