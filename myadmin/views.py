from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from users.forms import CustomUserCreationForm
from .forms import AdminLoginForm
from users.decorators import unauthorised_user
from users.models import ContactUs

# Create your views here.

User = get_user_model()

# signup view for myadmin


class AdminSignUpView(View):
    form_class = CustomUserCreationForm
    template_name = 'myadmin/admin_signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True
            user.save()

            # send registration code to email
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']

            admin = User.objects.get(username=username)
            reg_code = admin.code_number

            subject = 'Login Registration Code'
            message = f'The Login Registration Code for {first_name} {last_name} is {reg_code}.' \
                      f'It consists of 7 digit numbers and 3 capital letters (case sensitive).'
            sender = 'mayordecoder@gmail.com'
            recipient = 'akinade.mayowa@gmail.com'

            send_mail(subject, message, sender, [recipient], fail_silently=False)
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
            return render(request, 'myadmin/admin_signup_success.html', context)
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


# myadmin login user
@login_required
@unauthorised_user
def admin_user_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'], unique_id=cd['registration_number'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'myadmin/admin_welcome.html')
    else:
        form = AdminLoginForm()
    return render(request, 'myadmin/admin_login.html', {'form': form})


@login_required
@unauthorised_user
def list_users(request):
    users = User.objects.all()
    return render(request, 'myadmin/user_list.html', {'users': users})


@login_required
@unauthorised_user
def user_details(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'myadmin/user_details.html', {'user': user})


@login_required
@unauthorised_user
def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        if request.POST.get('yes') == 'Yes':
            user.delete()
            return HttpResponseRedirect('/users/list_users/')
        else:
            return HttpResponseRedirect('/users/list_users/')
    return render(request, 'myadmin/delete_user.html', {'user': user})


# view contact us messages

@login_required
@unauthorised_user
def contact_messages(request):
    messages = ContactUs.objects.all()
    return render(request, 'myadmin/messages_list.html', {'messages': messages})


@login_required
@unauthorised_user
def contact_details(request, id):
    message = get_object_or_404(ContactUs, id=id)
    return render(request, 'myadmin/messages_details.html', {'message': message})
