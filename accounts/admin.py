from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import BaseUserManager  # BaseUserManager を追加

from .models import User
# from .models import CustomUser
# from django.db import models
# from django.contrib.admin.models import LogEntry
# from django.utils.translation import gettext as _



# class UserAdmin(BaseUserAdmin):
#     list_display = ('account_id', 'email', 'is_staff', 'is_active')
#     ordering = ('account_id',)


# class UserAdmin(BaseUserAdmin):
class UserAdmin(BaseUserAdmin): 
    list_display = ('account_id', 'email', 'is_staff', 'is_active')
    ordering = ('account_id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

# class CustomLogEntry(LogEntry):
#     custom_user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('user'))



# class UserAdmin(BaseUserAdmin):
#     list_display = ('account_id', 'email', 'is_staff', 'is_active')
#     ordering = ('account_id',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )


    
admin.site.register(User, UserAdmin) 
# admin.site.register(CustomLogEntry)
admin.site.unregister(Group)

