from django.contrib import admin
from .models import *

# Register your models here.


class CategoryMusicAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class SingerAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class MusicMp3Admin(admin.ModelAdmin):
    fields = [
        "name_kurd",
        "name_persian",
        "name_english",
        "category",
        "signer",
        "kurd_date",
        "persian_date",
        "english_date",
        "popularity_rate",
        "music",
        "image",
        "cast_kurdish",
        "cast_persian",
        "cast_english",
    ]
    list_display = ["name_persian", "signer"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class MusicVideoAdmin(admin.ModelAdmin):
    fields = [
        "name_kurd",
        "name_persian",
        "name_english",
        "category",
        "signer",
        "kurd_date",
        "persian_date",
        "english_date",
        "popularity_rate",
        "music",
        "image",
        "cast_kurdish",
        "cast_persian",
        "cast_english",
    ]
    list_display = ["name_persian", "signer"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


admin.site.register(CategoryMusicModel, CategoryMusicAdmin)
admin.site.register(SingerModel, SingerAdmin)
admin.site.register(MusicMp3Model, MusicMp3Admin)
admin.site.register(MusicVideoModel, MusicVideoAdmin)
