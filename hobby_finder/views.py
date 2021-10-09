from django.contrib.auth import login
from django.shortcuts import (
    HttpResponseRedirect,
   	get_object_or_404,
    redirect,
    render
       
)

# from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction


from django.contrib.auth.forms import UserCreationForm
from events.models import Event
from .forms import UserForm, ProfileForm, EventForm

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'feed.html')
    else:
        return render(request, 'base.html')


def hobby(request):
    return render(request, 'hobby.html')


def registerPage(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)



def eventcreation(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()

    context = {'form': form}
    return render(request, 'event_creation.html', context)



def index(request):
    events_object = Event.objects.all()
    context = {
        "events": events_object
    }
    return render(request, 'feed.html', context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'), fail_silently=True) #used to be underscores here? just left of string in parentheses
            return redirect(update_profile)
        else:
            messages.error(request, ('Please correct the error below.'), fail_silently=True) #used to be underscores here? just left of string in parentheses
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })