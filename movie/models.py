from django.db import models
import os
from django.utils.html import mark_safe
from user.models import *

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"file/{final_name}"
    return x


class ActorModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام بازیگر کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام بازیگر فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام بازیگر انگلیسی")

    class Meta:
        verbose_name = "نام بازیگران"
        verbose_name_plural = "نام بازیگران"

    def __str__(self):
        return self.name_persian


class GenreModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام ژانر کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام ژانر فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام ژانر انگلیسی")

    class Meta:
        verbose_name = "ژانر"
        verbose_name_plural = "ژانر"

    def __str__(self):
        return self.name_persian


class DirectorModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام کارگردان کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام کارگردان فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام کارگردان انگلیسی")

    class Meta:
        verbose_name = "کارگردان"
        verbose_name_plural = "کارگردان"

    def __str__(self):
        return self.name_persian


class CategoryModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام دسته کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام دسته فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام دسته انگلیسی")

    class Meta:
        verbose_name = "دسته ها "
        verbose_name_plural = "دسته ها "

    def __str__(self):
        return self.name_persian


class AwardsModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام جایزه کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام جایزه فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام جایزه انگلیسی")

    class Meta:
        verbose_name = "جایزه ها "
        verbose_name_plural = "جایزه ها "

    def __str__(self):
        return self.name_persian


class ProducerModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام تهیه کننده کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام تهیه کننده فارسی")
    name_english = models.CharField(
        max_length=100, verbose_name="نام تهیه کننده انگلیسی"
    )

    class Meta:
        verbose_name = "تهیه کننده ها "
        verbose_name_plural = "تهیه کننده ها "

    def __str__(self):
        return self.name_persian


class MovieModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام فیلم کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام فیلم فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام فیلم انگلیسی")
    actor = models.ManyToManyField(ActorModel, verbose_name="نام بازیگران")
    genre = models.ForeignKey(GenreModel, verbose_name="ژانر", on_delete=models.CASCADE)
    category = models.ForeignKey(
        CategoryModel, verbose_name="دسته", on_delete=models.CASCADE
    )
    director = models.ForeignKey(
        DirectorModel, verbose_name="کارگردان", on_delete=models.CASCADE
    )
    award = models.ManyToManyField(
        AwardsModel, verbose_name="جایزه ها "
    )
    producer = models.ManyToManyField(ProducerModel, verbose_name="تهیه کننده ها ")
    kurd_date = models.CharField(verbose_name="تاریخ کردی", max_length=20)
    persian_date = models.CharField(verbose_name="تاریخ فارسی", max_length=20)
    english_date = models.CharField(verbose_name="تاریخ انگلیسی", max_length=20)
    kurd_description = models.TextField(verbose_name="خلاصه فیلم کردی")
    persian_description = models.TextField(verbose_name="خلاصه فیلم فارسی")
    english_description = models.TextField(verbose_name="خلاصه فیلم انگلیسی")
    imdb = models.CharField(
        verbose_name="نمره imdb", max_length=5, null=True, blank=True
    )
    popularity_rate = models.FloatField(
        verbose_name="میزان محبوبیت", null=True, blank=True
    )
    movie = models.FileField(verbose_name="فیلم", upload_to=file_path, max_length=2000)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=file_path,
        verbose_name="عکس فیلم",
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    def __str__(self):
        return self.name_persian
