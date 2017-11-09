# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 01:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0002_auto_20171109_0155'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userexercise',
            unique_together=set([('user', 'exercise')]),
        ),
    ]