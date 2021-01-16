from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
