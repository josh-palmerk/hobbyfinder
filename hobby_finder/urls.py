from django.contrib import admin
from django.urls import include, path
from . import views
# from .views import homepage, registerPage, update_profile, eventcreation
# from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', include('events.urls')),
    path('', views.homepage),
    # path('hobby/', views.hobby),
    # path('events/', views.events),
    path('register/', views.registerPage, name='registerPage'),
    path('profile/', views.update_profile),
    path('create_event/', views.eventcreation),

    path('', views.index, name='index'),
]
