# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 11:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codesample', '0008_auto_20160814_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 11, 20, 49, 987346)),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='name',
            field=models.CharField(default=b'20160814_112049', max_length=20),
        ),
    ]
