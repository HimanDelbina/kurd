from django.contrib import admin
from .models import *

# Register your models here.


class ActorAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class GenreAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class DirectorAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["name_kurd", "name_persian", "name_english"]
    list_display = ["name_kurd", "name_persian", "name_english"]
    search_fields = ["name_kurd", "name_persian", "name_english"]


class MovieAdmin(admin.ModelAdmin):
    fields = [
        "name_kurd",
        "name_persian",
        "name_english",
        "actor",
        "genre",
        "category",
        "director",
        "kurd_date",
        "persian_date",
        "english_date",
        "kurd_description",
        "persian_description",
        "english_description",
        "imdb",
        "popularity_rate",
        "movie",
        "image",
    ]
    list_display = [
        "name_persian",
        "persian_date",
        "imdb",
        "popularity_rate",
        "image_tag",
    ]
    search_fields = ["name_kurd", "name_persian", "name_english"]


admin.site.register(ActorModel, ActorAdmin)
admin.site.register(GenreModel, GenreAdmin)
admin.site.register(DirectorModel, DirectorAdmin)
admin.site.register(MovieModel, MovieAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
