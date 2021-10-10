from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.


class Event(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(default=timezone.now)
    # creator = models.CharField(max_length=50, null=False, blank=False)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
