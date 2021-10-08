from django.shortcuts import (
    HttpResponseRedirect,
   	get_object_or_404,
    render
)
from .models import Events

def homepage(request):
    if request.user.is_authenticated:
        ... # Do something for logged-in users.
    else:
        return render(request, 'base.html')



def hobby(request):
    return render(request, 'hobby.html')


def events(request):
    events_object = Events.objects.all()
    context = {
        "events_object": events_object
    }
    return render(request, 'events.html', context)


#                                           CHECK USER AUTHENTICATION
