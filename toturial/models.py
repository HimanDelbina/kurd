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


class ToturialModel(models.Model):
    title_kurd = models.CharField(max_length=100, verbose_name="نام آموزش کردی")
    title_persian = models.CharField(max_length=100, verbose_name="نام آموزش فارسی")
    title_english = models.CharField(max_length=100, verbose_name="نام آموزش انگلیسی")
    kurd_description = models.TextField(verbose_name="شرح آموزش کردی")
    persian_description = models.TextField(verbose_name="شرح آموزش فارسی")
    english_description = models.TextField(verbose_name="شرح آموزش انگلیسی")
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="Toturial",
        verbose_name="عکس آموزش",
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
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها"

    def __str__(self):
        return self.title_persian
