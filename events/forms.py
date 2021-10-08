from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"  # include all fields
        # exclude = ['isactive'] # exclude example if we dont want something displayed to user
