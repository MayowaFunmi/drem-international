from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('admin_signup/', views.AdminSignUpView.as_view(), name='admin_signup'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('admin_login/', views.admin_user_login, name='admin_login'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('testimony/', views.testimony, name='testimony'),
    path('prayer_request/', views.prayer_request, name='prayer_request'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('list_users/', views.list_users, name='list_users'),
    path('user_details/<int:id>/', views.user_details, name='user_details'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('home/', views.base, name='home'),
]