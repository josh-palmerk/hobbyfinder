from django import forms
from events.models import User, Profile


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