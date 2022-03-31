from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session

from .forms import CustomUserCreationForm, CustomUserChangeForm


User = get_user_model()

admin.site.register(User)
'''
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'code_number', 'first_name', 'last_name']

admin.site.register(User, CustomUserAdmin)
'''

class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.site_header = 'DREM INTERNATIONAL ADMIN PAGE'
admin.site.register(Session, SessionAdmin)
