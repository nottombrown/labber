from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

class PersonType(models.Model):
    """Either Professor, PostDoc, GradStudent or Undergrad"""
    type = models.CharField(max_length=200)

class ResearchTopic(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

class Publication(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    
class Sponsors(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)