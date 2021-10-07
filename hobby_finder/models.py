from django.db import models


class Events(models.Model):

    '''
    Create the events table in the database
    '''
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=True)
    location = models.CharField(max_length=300, null=False, blank=True)
    is_active = models.BooleanField(default=True)
    tags = models.CharField(max_length=(50), blank=True)


'''
# TODO: 
We need to figure out a one to many relationship between tags and Events
'''


class Hobby_Tags(models.Model):

    '''
    Create the tags table in the databases
    '''
    name = models.CharField(max_length=(50), blank=True)
