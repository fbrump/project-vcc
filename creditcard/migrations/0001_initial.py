# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 04:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CreditCard',
                'verbose_name_plural': 'CreditCards',
            },
        ),
    ]
