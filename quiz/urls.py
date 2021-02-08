from django.urls import path
from . import views
app_name = 'quiz'

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('index/', views.index, name='index'),
    path('save_ans/', views.save_ans, name='save_ans'),
    path('result/', views.result, name='result'),
    path('add_quiz', views.add_question, name='add_quiz'),
    path('all_questions/', views.all_questions, name='all_questions'),
]
