from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "email", "password"]
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]



admin.site.register(UserModel, UserAdmin)
