# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_auto_20160926_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna',
            name='reply',
        ),
        migrations.AddField(
            model_name='qna',
            name='answer',
            field=models.TextField(null=True, verbose_name='Answer.'),
        ),
    ]
