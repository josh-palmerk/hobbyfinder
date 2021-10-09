
"""
IMPORTANT: All urls should be placed under 
hobby_finder.urls
for some reason django only grabs them from there.
beats me as to why but it's not hard to code around
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_event/', views.eventcreation),
]
