import imp
from django.contrib import admin
from .models import Account

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'last_login']

admin.site.register(Account, MyUserAdmin)
