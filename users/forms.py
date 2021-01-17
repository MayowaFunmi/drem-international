from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import ContactUs, Testimony, PrayerRequest

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
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Surname'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Middle Name'}),
            'church_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Name Of Your Church'}),
            #'marital_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose Your Marital Status'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address'}),
            'favourite_bible_verse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your favourite bible passage?'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell Us Something About Yourself (not more than 300 words)...'}),
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
        fields = ('testimony', )


# Prayer request form
class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ('prayer_points', )