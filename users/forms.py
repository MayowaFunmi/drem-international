from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import ContactUs, Testimony

User = get_user_model()

# User sign up form


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'middle_name', 'born_again', 'church_name',
            'marital_status', 'address', 'phone_number', 'date_of_birth', 'photo', 'favourite_bible_verse', 'about_me'
        )
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

# contact us form

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


# login form
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


# testimony form
class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = '__all__'