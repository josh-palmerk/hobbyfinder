from django.contrib import admin

from .models import Tag, EventTag, UserTag

admin.site.register(Tag)
admin.site.register(EventTag)
admin.site.register(UserTag)
