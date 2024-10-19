from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ["username",  "email", "password"]
    list_display = ["username", "email"]
    search_fields = ["username", "email"]



admin.site.register(UserModel, UserAdmin)
