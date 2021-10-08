from django.urls import reverse
from django.db import models


class Events(models.Model):

    '''
    Create the events table in the database
    '''
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=True)
    location = models.CharField(max_length=300, null=False, blank=True)
    is_active = models.BooleanField(default=True)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE)


'''
# TODO:
We need to figure out a one to many relationship between tags and Events
'''


class Tags(models.Model):

    '''
    Create the tags table in the databases
    '''
    name = models.CharField(max_length=(50), blank=True)


# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=(255), null=False, blank=False)
    email = models.CharField(max_length=(255), null=False, blank=False)
    password = models.CharField(max_length=(255), null=False, blank=False)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
