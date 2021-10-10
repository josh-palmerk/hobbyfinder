from django.contrib.auth import authenticate, login, logout
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


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from events.models import Event, User
from tags.models import Tag, EventTag, UserTag
from .forms import UserForm, ProfileForm, EventForm
from django.contrib.auth.views import LoginView, redirect_to_login


def homepage(request):
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


@login_required(login_url='/login/')
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # used to be underscores here? just left of string in parentheses
            messages.success(
                request, ('Your profile was successfully updated!'), fail_silently=True)
            return redirect(update_profile)
        else:
            # used to be underscores here? just left of string in parentheses
            messages.error(
                request, ('Please correct the error below.'), fail_silently=True)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
<<<<<<< HEAD

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!", fail_silently=True)
    return redirect(homepage)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "login.html",
                  context={"form":form})



# class AdminLogin(LoginView):
#     template_name = 'login.html'



# def login(request):
#     username = request.POST[User.username]
#     password = request.POST[User.password]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         redirect(homepage)
#     else:
#         # Return an 'invalid login' error message.
#         redirect(homepage)from django.contrib.auth.views import LoginView
=======
>>>>>>> 74f06a7 (Tag logic in events/views.py)
