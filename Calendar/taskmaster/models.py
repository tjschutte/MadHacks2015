from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Task(models.Model):
    dueDate = models.DateTimeField('Due Date', null = True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    category = models.ForeignKey('Category')

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    color = models.ForeignKey('Color')

class Event(models.Model):
    startDate = models.DateTimeField('Start')
    endDate = models.DateTimeField('End')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    category = models.ForeignKey('Category')
    
class Color(models.Model):
    R = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
     )
    G = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
     )
    B = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
     )
