# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 05:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codesample', '0020_auto_20160816_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 5, 10, 54, 713655)),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='name',
            field=models.CharField(default=b'20160816_051054', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='dp',
            field=models.FileField(upload_to='dps/%Y%m%d'),
        ),
    ]
