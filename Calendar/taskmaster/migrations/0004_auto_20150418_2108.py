# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0003_auto_20150418_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, to='taskmaster.Category', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(null=True, verbose_name=b'Due Date', blank=True),
        ),
    ]
