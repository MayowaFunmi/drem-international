from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# myadmin login form


class AdminLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    registration_number = forms.CharField(widget=forms.PasswordInput, required=True)