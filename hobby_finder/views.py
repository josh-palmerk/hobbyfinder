from django.shortcuts import (
    HttpResponseRedirect,
   	get_object_or_404,
    render
)


def homepage(request):
    return render(request, 'base.html')


def hobby(request):
    return render(request, 'hobby.html')


def events(request):
    return render(request, 'events.html')


#                                           CHECK USER AUTHENTICATION
#     if request.user.is_authenticated:
#     ... # Do something for logged-in users.
# else:
#     ... # Do something for anonymous users.
