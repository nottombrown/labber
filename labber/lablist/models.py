from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class LabMember(User):
    """Either Professor, PostDoc, GradStudent or Undergrad"""
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
class Professor(LabMember):
    """"""
    
class PostDoc(LabMember):
    """"""

class GradStudent(LabMember):
    """"""

class UnderGrad(LabMember):
    """"""


class ResearchTopic(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

class Publication(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)