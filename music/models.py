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
    x = f"music/{final_name}"
    return x


class CategoryMusicModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام دسته بندی کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام دسته بندی فارسی")
    name_english = models.CharField(
        max_length=100, verbose_name="نام دسته بندی انگلیسی"
    )

    class Meta:
        verbose_name = "نام دسته بندی"
        verbose_name_plural = "نام دسته بندی"

    def __str__(self):
        return self.name_persian


class SingerModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام خواننده کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام خواننده فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام خواننده انگلیسی")

    class Meta:
        verbose_name = "نام خواننده"
        verbose_name_plural = "نام خواننده"

    def __str__(self):
        return self.name_persian


class MusicMp3Model(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام موزیک کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام موزیک فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام موزیک انگلیسی")
    category = models.ForeignKey(
        CategoryMusicModel, verbose_name="دسته", on_delete=models.CASCADE
    )
    signer = models.ForeignKey(
        SingerModel, verbose_name="خواننده", on_delete=models.CASCADE
    )
    kurd_date = models.CharField(verbose_name="تاریخ کردی", max_length=20)
    persian_date = models.CharField(verbose_name="تاریخ فارسی", max_length=20)
    english_date = models.CharField(verbose_name="تاریخ انگلیسی", max_length=20)
    popularity_rate = models.FloatField(verbose_name="میزان محبوبیت", default=0.0)
    music = models.FileField(verbose_name="موزیک", upload_to=file_path, max_length=100)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=file_path,
        verbose_name="عکس موزیک",
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
        verbose_name = "موزیک"
        verbose_name_plural = "موزیک صوتی"

    def __str__(self):
        return self.name_persian


class MusicVideoModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام موزیک کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام موزیک فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام موزیک انگلیسی")
    category = models.ForeignKey(
        CategoryMusicModel, verbose_name="دسته", on_delete=models.CASCADE
    )
    signer = models.ForeignKey(
        SingerModel, verbose_name="خواننده", on_delete=models.CASCADE
    )
    kurd_date = models.CharField(verbose_name="تاریخ کردی", max_length=20)
    persian_date = models.CharField(verbose_name="تاریخ فارسی", max_length=20)
    english_date = models.CharField(verbose_name="تاریخ انگلیسی", max_length=20)
    popularity_rate = models.FloatField(verbose_name="میزان محبوبیت", default=0.0)
    music = models.FileField(verbose_name="موزیک", upload_to=file_path, max_length=1000)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=file_path,
        verbose_name="عکس موزیک",
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
        verbose_name = "موزیک"
        verbose_name_plural = "موزیک تصویری"

    def __str__(self):
        return self.name_persian
