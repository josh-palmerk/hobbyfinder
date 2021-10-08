from django.shortcuts import render
from .models import Event

# Create your views here.


def index(request):
    events_object = Event.objects.all()
    context = {
        "events": events_object
    }
    return render(request, 'feed.html', context)
