from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Event(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    time_created = models.DateTimeField('date published')
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




# TODO: add a creator field to event class ^^

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()