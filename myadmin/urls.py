from django.urls import path
from . import views

app_name = 'myadmin'

urlpatterns = [
    path('admin_signup/', views.AdminSignUpView.as_view(), name='admin_signup'),
    path('admin_login/', views.admin_user_login, name='admin_login'),
    path('list_users/', views.list_users, name='list_users'),
    path('user_details/<int:id>/', views.user_details, name='user_details'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
]