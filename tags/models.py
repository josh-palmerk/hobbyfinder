from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.


class Tag(models.Model):

    name = models.CharField(max_length=50)


class EventTag(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class UserTag(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
