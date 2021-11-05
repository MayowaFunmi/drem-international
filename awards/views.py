import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AwardForm
from .models import Awards
from users.decorators import unauthorised_user


@login_required
@unauthorised_user
def award_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        name = request.POST['name']
        award_title = request.POST['award_title']
        award_image_1 = request.FILES['award_image_1']
        award_image_2 = request.FILES['award_image_2']
        brief_profile = request.POST['brief_profile']

        awards = Awards.objects.create(
            title=title, name=name, award_title=award_title, award_image_1=award_image_1, award_image_2=award_image_2,
            brief_profile=brief_profile
        )
        awards.save()
        get_photo = Awards.objects.get(id=awards.id)
        context = {
            'title': title, 'name': name, 'award_title': award_title, 'award_image_1': get_photo.award_image_1,
            'award_image_2': get_photo.award_image_2, 'brief_profile': brief_profile
        }
        return render(request, 'awards/biography_detail.html', context)

    return render(request, 'awards/biography_form.html')


def award_list(request):
    all_awards = Awards.objects.all().order_by('pk')
    paginator = Paginator(all_awards, 1)
    page = request.GET.get('page')
    awards = paginator.get_page(page)
    context = {
        'awards': awards,
    }
    return render(request, 'awards/awards_list.html', context)


@login_required
@unauthorised_user
def delete_award(request, id):
    award = get_object_or_404(Awards, id=id)
    if request.method == 'POST':
        ask = request.POST['ask']
        if ask == 'Yes':
            award.delete()
            return redirect('/awards/list_awards/')
        elif ask == 'No':
            return redirect('/awards/list_awards/')
    return render(request, 'awards/delete_award.html', {'award': award})
