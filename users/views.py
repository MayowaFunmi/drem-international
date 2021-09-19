from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .decorators import unauthorised_user
from .forms import CustomUserCreationForm, ContactUsForm, LoginForm, TestimonyForm, PrayerRequestForm

User = get_user_model()


def base(request):
    return render(request, 'users/base.html')


class UserSignUpView(View):
    form_class = CustomUserCreationForm
    template_name = 'users/user_signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            photo = request.FILES['photo']
            fs = FileSystemStorage()
            photo_filename = fs.save(photo.name, photo)

            context = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'middle_name': form.cleaned_data['middle_name'],
                'born_again': form.cleaned_data['born_again'],
                'church_name': form.cleaned_data['church_name'],
                'marital_status': form.cleaned_data['marital_status'],
                'address': form.cleaned_data['address'],
                'phone_number': form.cleaned_data['phone_number'],
                'date_of_birth': form.cleaned_data['date_of_birth'],
                'favourite_bible_verse': form.cleaned_data['favourite_bible_verse'],
                'about_me': form.cleaned_data['about_me'],
                'photo': fs.url(photo_filename),
            }
            return render(request, 'users/signup_success.html', context)

        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


# login view

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/base.html')
            else:
                messages.error(request, 'Incorrect Username or Password')
                return render(request, 'users/login.html', {'form': form})

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# user Profile


@login_required
def user_profile(request):
    if User.objects.filter(username=request.user.username).exists():
        user = User.objects.get(username=request.user.username)
        return render(request, 'users/user_profile.html', {'user': user})

# logout view


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/home/')

# view for contact form


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        try:
            if form.is_valid():
                form.save(commit=True)

                return render(request, 'users/contact_us_success.html')
        except:
            return render(request, 'users/errors.html')

    else:
        form = ContactUsForm()

    return render(request, 'users/contact_us.html', {'form': form})


# testimony form
@login_required
def testimony(request):
    user = request.user
    if request.method == 'POST':
        form = TestimonyForm(request.POST)

        try:
            if form.is_valid():
                myform = form.save(commit=False)
                myform.user = request.user
                myform.save()

                context = {
                    'user': request.user.username,
                    'testimony': form.cleaned_data['testimony']
                }

                return render(request, 'users/testimony_detail.html', context)
        except:
            return render(request, 'users/errors.html')

    else:
        form = TestimonyForm()
    return render(request, 'users/testimony_form.html', {'form': form, 'user': user})


# prayer request form
@login_required
def prayer_request(request):
    user = request.user
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)

        try:
            if form.is_valid():
                myform = form.save(commit=False)
                myform.user = request.user
                myform.save()

                context = {
                    'user': request.user,
                    'prayer_points': form.cleaned_data['prayer_points']
                }

                return render(request, 'users/prayer_request_detail.html', context)
        except:
            return render(request, 'users/errors.html')

    else:
        form = TestimonyForm()
    return render(request, 'users/prayer_request_form.html', {'form': form, 'user': user})


# update user profile

@login_required
def update_user(request):
    obj = get_object_or_404(User, id=request.user.id)
    form = CustomUserCreationForm(request.POST or None, instance=obj)

    try:
        if form.is_valid():
            form.save(commit=True)
            user = User.objects.get(username=request.user.username)
            return render(request, 'users/user_profile.html', {'user': user})

    except:
        return render(request, 'users/errors.html')

    return render(request, 'users/update_user_profile.html', {'form': form})


def about_us(request):
    return render(request, 'users/about_us.html')


def convener(request):
    return render(request, 'users/convener.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password Has Been Changed Successfully')
            return redirect('users:logout')
        else:
            messages.error(request, 'Error while changing your password. Please try again')
            return redirect('users:change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
