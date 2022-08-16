from django import forms
from .models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
    patronymic = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'password',
        )