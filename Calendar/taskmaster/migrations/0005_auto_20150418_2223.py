# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0004_auto_20150418_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(verbose_name=b'startDate'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, to='taskmaster.Category', null=True),
        ),
    ]
