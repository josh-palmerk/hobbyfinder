
"""
IMPORTANT: All views should be placed under
hobby_finder.views  so that  hobby_finder.urls
can grab it properly :)
"""


from django.shortcuts import render
from .models import Event
from .forms import EventForm
from tags.models import Tag, UserTag, EventTag

# Create your views here.

# .order_by .filter


def index(request):

    if request.user.is_authenticated:
        user_tags = UserTag.objects.all().filter(user.username == User.username)
        events = []
        for tag in user_tags:
            events.append(EventTag.objects.all().filter(
                tag.tag.name == EventTag.tag.name))
        context = {'event': events}
        return render(request, 'feed.html', context)
    else:
        events_object = Event.objects.all()
        context = {'event': events_object}
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
