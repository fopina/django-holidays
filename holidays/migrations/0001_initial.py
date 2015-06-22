# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('identifier', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(to='holidays.Group', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=50, verbose_name=b'Rule Type', choices=[(b'easter_sunday', b'Easter sunday'), (b'fixed_date', b'Fixed day in month'), (b'n_days_before_rule', b'N days before rule X')])),
                ('parameters', models.CharField(max_length=50, null=True, blank=True)),
                ('group', models.ForeignKey(to='holidays.Group')),
            ],
        ),
    ]
