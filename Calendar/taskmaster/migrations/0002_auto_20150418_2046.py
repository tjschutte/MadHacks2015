# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(null=True, verbose_name=b'Due Date'),
        ),
    ]
