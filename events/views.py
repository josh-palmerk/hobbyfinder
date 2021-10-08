from django.shortcuts import render
from .models import Event
from .forms import EventForm

# Create your views here.

# .order_by .filter


def index(request):
    events_object = Event.objects.all()
    context = {
        "events": events_object
    }
    return render(request, 'feed.html', context)


def eventcreation(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()

    context = {'form': form}
    return render(request, 'event_creation.html', context)
