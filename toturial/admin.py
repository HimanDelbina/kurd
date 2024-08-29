from django.contrib import admin
from .models import *

# Register your models here.


class ToturialAdmin(admin.ModelAdmin):
    fields = [
        "title_kurd",
        "title_persian",
        "title_english",
        "kurd_description",
        "persian_description",
        "english_description",
        "image",
    ]
    list_display = [
        "title_persian",
        "image_tag",
    ]
    search_fields = ["title_persian"]


admin.site.register(ToturialModel, ToturialAdmin)
