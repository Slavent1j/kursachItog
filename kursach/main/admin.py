from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_role', 'phone')
    UserAdmin.fieldsets += (('Extra Fields', {'fields': ('user_role', 'phone', 'address')}),)
