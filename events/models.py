from django.db import models

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
