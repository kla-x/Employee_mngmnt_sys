from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Department, Role
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone_number', 'department', 'role', 'bank_account_number', 'is_approved', 'is_dep_lead', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_approved', 'is_dep_lead')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('phone_number', 'department', 'role', 'bank_account_number', 'is_approved', 'is_dep_lead', 'profile_picture')}),
    )



admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Role)