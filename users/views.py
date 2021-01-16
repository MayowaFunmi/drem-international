from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import View
from .forms import CustomUserCreationForm, ContactUsForm, LoginForm, TestimonyForm


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
            return render(request, 'users/signup_success.html')
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
                    return render(request, 'users/home.html')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


# logout view

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'users/home.html')


# view for contact form

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request, 'users/contact_us_success.html')
        else:
            print(form.errors)
            print("Invalid Form")
    else:
        form = ContactUsForm()

    return render(request, 'users/contact_us.html', {'form': form})


# testimony form

def testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request, 'users/testimony_detail.html')
    else:
        form = TestimonyForm()

    return render(request, 'users/testimony_form.html', {'form': form})
