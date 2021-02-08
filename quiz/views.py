from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render
from .models import Questions
from .forms import QuizForm
from users.decorators import unauthorised_user

lst = []
answers = Questions.objects.all()
anslist = []

for i in answers:
    anslist.append(i.answer)


def index(request):
    obj = Questions.objects.all()
    count = obj.count()
    paginator = Paginator(obj, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        questions = paginator.page(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz/index.html', {'obj': obj, 'questions': questions, 'count': count})


@login_required
def result(request):
    score = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 1
    return render(request, 'quiz/result.html', {'score': score, 'lst': lst})


def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)


def welcome(request):
    lst.clear()
    return render(request, 'quiz/welcome.html')

@login_required
@unauthorised_user
def add_question(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            context = {
                'question': form.cleaned_data['question'],
                'option1': form.cleaned_data['option1'],
                'option2': form.cleaned_data['option2'],
                'option3': form.cleaned_data['option3'],
                'option4': form.cleaned_data['option4'],
                'answer': form.cleaned_data['answer'],
            }

            return render(request, 'quiz/questions.html', context)

    else:
        form = QuizForm()
    return render(request, 'quiz/add_questions.html', {'form': form})


@login_required
@unauthorised_user
def all_questions(request):
    questions = Questions.objects.all().order_by('pk')
    return render(request, 'quiz/all_questions.html', {'questions': questions})