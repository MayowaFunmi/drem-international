from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import AwardForm
from .models import Awards
from users.decorators import unauthorised_user


@login_required
@unauthorised_user
def award_view(request):
    if request.method == 'POST':
        form = AwardForm(data=request.POST, files=request.FILES)

        try:
            if form.is_valid():
                form.save(commit=True)

                award_image_1 = request.FILES['award_image_1']
                fs = FileSystemStorage()
                award_image_1_filename = fs.save(award_image_1.name, award_image_1)

                award_image_2 = request.FILES['award_image_2']
                fs = FileSystemStorage()
                award_image_2_filename = fs.save(award_image_2.name, award_image_2)

                context = {
                    'title': form.cleaned_data['title'],
                    'name': form.cleaned_data['name'],
                    'award_title': form.cleaned_data['award_title'],
                    'award_image_1': fs.url(award_image_1_filename),
                    'award_image_2': fs.url(award_image_2_filename),
                    'brief_profile': form.cleaned_data['brief_profile'],
                }
                return render(request, 'awards/biography_detail.html', context)
        except:
            return render(request, 'users/errors.html')

    else:
        form = AwardForm()
    return render(request, 'awards/biography_form.html', {'form': form})


@login_required
def award_list(request):
    all_awards = Awards.objects.all()
    paginator = Paginator(all_awards, 1)
    page = request.GET.get('page')
    awards = paginator.get_page(page)
    return render(request, 'awards/awards_list.html', {'awards': awards})


@login_required
@unauthorised_user
def delete_award(request, id):
    award = get_object_or_404(Awards, id=id)

    if request.method == 'POST':
        if request.POST.get('yes') == 'Yes':
            award.delete()
            return HttpResponseRedirect('/awards/list_awards/')
        else:
            return HttpResponseRedirect('/awards/list_awards/')
    return render(request, 'awards/delete_award.html', {'award': award})
