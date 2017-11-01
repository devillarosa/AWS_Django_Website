# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 17:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('completed_sets', models.IntegerField()),
                ('max_sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exercise_list', models.ManyToManyField(to='fitness.Exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.ExerciseName'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
