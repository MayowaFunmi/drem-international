from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('testimony/', views.testimony, name='testimony'),
    path('base/', views.base),
]