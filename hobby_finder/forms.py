from django import forms
from events.models import User, Profile, Event


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Register


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"  # include all fields
        # These are automatically filled so exclude from form
        exclude = ['is_active', 'time_created']
