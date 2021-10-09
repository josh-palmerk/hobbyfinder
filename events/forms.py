from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"  # include all fields
        # These are automatically filled so exclude from form
        exclude = ['is_active', 'time_created']
