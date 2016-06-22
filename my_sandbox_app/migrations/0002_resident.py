# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 02:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_sandbox_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_sandbox_app.TriStatePlace')),
            ],
        ),
    ]
