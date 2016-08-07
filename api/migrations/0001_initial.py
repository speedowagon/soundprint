# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soundprint', models.FileField(max_length=64, upload_to=b'')),
                ('message', models.CharField(max_length=512)),
            ],
        ),
    ]