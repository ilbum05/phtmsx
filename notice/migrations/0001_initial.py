# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faq', '0007_auto_20160926_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_kind', enumchoicefield.fields.EnumChoiceField(enum_class=notice.models.Enum_Kind, max_length=2)),
                ('owner', models.CharField(max_length=20, null=True, verbose_name='Owner.')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject.')),
                ('counter', models.SmallIntegerField(verbose_name='Counter')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('attach', models.FileField(blank=True, upload_to='uploads/notice/%Y/%m/%d/', verbose_name='Attachment.')),
                ('cdate', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('mdate', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('buz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.Company')),
            ],
            options={
                'verbose_name_plural': 'notices',
                'ordering': ['-mdate'],
                'db_table': 'notice',
            },
        ),
    ]
