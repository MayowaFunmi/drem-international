from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ApplicationForm, ApplicationCode
from .models import Application


@login_required
def application_form(request):
    return render(request, 'bible_school/application_form.html')


@login_required
def application_form_save(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        place_of_birth = request.POST['place_of_birth']
        phone_number = request.POST['phone_number']
        marital_status = request.POST['marital_status']
        name_of_spouse = request.POST['spouse']
        number_of_children = request.POST['children_number']
        children_age_bracket = request.POST['children_age']
        course_of_study = request.POST['course_of_study']
        country_of_residence = request.POST['country_of_residence']
        state_or_city_1 = request.POST['state_or_city_1']
        residential_address = request.POST['residential_address']
        country_of_origin = request.POST['country_of_origin']
        state_or_city_2 = request.POST['state_or_city_2']
        permanent_address = request.POST['permanent_address']
        years_born_again = request.POST['years_born_again']
        salvation_experience = request.POST['salvation_experience']
        spirit_baptism = request.POST['spirit_baptism']
        spiritual_gifts = request.POST['spiritual_gifts']
        ministry_gift = request.POST['ministry_gift']
        spiritual_fruit = request.POST['spiritual_fruit']
        disability = request.POST['disability']
        discplined = request.POST['discplined']
        obedience = request.POST['obedience']
        ministry_experience = request.POST['ministry_experience']
        spiritual_mentor = request.POST['spiritual_mentor']

        try:
            form =Application(
                user=request.user.username,
                course_of_study=course_of_study,
                country_of_residence=country_of_residence,
                state_or_city_1=state_or_city_1,
                residential_address=residential_address,
                country_of_origin=country_of_origin,
                state_or_city_2=state_or_city_2,
                permanent_address=permanent_address,
                phone_number=phone_number,
                place_of_birth=place_of_birth,
                marital_status=marital_status,
                gender=gender,
                name_of_spouse=name_of_spouse,
                number_of_children=number_of_children,
                children_age_bracket=children_age_bracket,
                years_born_again=years_born_again,
                salvation_experience=salvation_experience,
                spirit_baptism=spirit_baptism,
                spiritual_gifts=spiritual_gifts,
                spiritual_fruit=spiritual_fruit,
                disability=disability,
                ministry_gift=ministry_gift,
                discplined=discplined,
                ministry_experience=ministry_experience,
                spiritual_mentor=spiritual_mentor,
                obedience=obedience
            )
            form.save()
            return render(request, 'bible_school/application_success.html')
        except:
            messages.error(request, "Your Application Failed")
            #return HttpResponseRedirect('/country/application_form/')
            return render(request, 'bible_school/application_form.html')
    else:
        return render(request, 'bible_school/application_form.html')


# bible school home page
def bible_school_home(request):
    return render(request, 'bible_school/sbi_home.html')


@login_required
def code_login(request):
    if request.method == 'POST':
        code = request.POST['login_code']
        if code == request.user.code_number:
            return redirect('school:apply')
        else:
            messages.error(request, "Incorrect Login Code")
    return redirect('school:sbi_home')


@login_required
def apply_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            if myform.obedience == False:
                messages.error(request, "You must agree to adhere strictly to the rules and regulations of S.B.I. Please check the box next to 'obedience' in the application form.")
                return render(request, 'bible_school/apply_form.html', {'form': form})
            else:
                myform.save()
            return render(request, 'bible_school/application_success.html')
    else:
        form = ApplicationForm()
    return render(request, 'bible_school/apply_form.html', {'form': form})