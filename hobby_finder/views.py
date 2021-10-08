from django.shortcuts import (
    HttpResponseRedirect,
   	get_object_or_404,
    render
)

from django.contrib.auth.forms import UserCreationForm
from events.models import Event


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
