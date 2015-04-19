# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('R', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('G', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('B', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateTimeField(verbose_name=b'Start')),
                ('endDate', models.DateTimeField(verbose_name=b'End')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(to='taskmaster.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dueDate', models.DateTimeField(verbose_name=b'Due Date')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(to='taskmaster.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.ForeignKey(to='taskmaster.Color'),
        ),
    ]
