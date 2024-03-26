from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfie

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin')
    ordering = ('-date_joined',)  # Corrected attribute name
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfie)
