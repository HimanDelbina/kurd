from django.contrib import admin
from .models import *

# Register your models here.


class CategoryPodcastAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class SingerPodcastAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class PodcastAdmin(admin.ModelAdmin):
    fields = [
        "name_kurd",
        "name_persian",
        "name_english",
        "category",
        "singer",
        "kurd_date",
        "persian_date",
        "english_date",
        "popularity_rate",
        "music",
        "writer_kurd",
        "writer_persian",
        "writer_english",
        "musictext_kurd",
        "musictext_persian",
        "musictext_english",
        "cast_kurdish",
        "cast_persian",
        "cast_english",
        "image",
    ]
    list_display = ["name_persian", "persian_date"]
    search_fields = ["name_persian"]


class PodcastVideoAdmin(admin.ModelAdmin):
    fields = [
        "name_kurd",
        "name_persian",
        "name_english",
        "category",
        "singer",
        "kurd_date",
        "persian_date",
        "english_date",
        "popularity_rate",
        "music",
        "writer_kurd",
        "writer_persian",
        "writer_english",
        "musictext_kurd",
        "musictext_persian",
        "musictext_english",
        "compilation_kurd",
        "compilation_persian",
        "compilation_english",
        "image",
        "cast_kurdish",
        "cast_persian",
        "cast_english",
    ]
    list_display = ["name_persian", "persian_date"]
    search_fields = ["name_persian"]


admin.site.register(PodcastModel, PodcastAdmin)
admin.site.register(PodcastVideoModel, PodcastVideoAdmin)
admin.site.register(CategoryPodcastModel, CategoryPodcastAdmin)
admin.site.register(SingerPodcastModel, SingerPodcastAdmin)
