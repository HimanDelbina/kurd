from django.db import models
import os
from django.utils.html import mark_safe



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"podcast/{final_name}"
    return x


class CategoryPodcastModel(models.Model):
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


class SingerPodcastModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام گوینده کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام گوینده فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام گوینده انگلیسی")

    class Meta:
        verbose_name = "نام خواننده"
        verbose_name_plural = "نام خواننده"

    def __str__(self):
        return self.name_persian


class PodcastModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام پادکست کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام پادکست فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام پادکست انگلیسی")
    category = models.ForeignKey(
        CategoryPodcastModel,
        verbose_name="دسته",
        on_delete=models.CASCADE,
        related_name="category",
    )
    singer = models.ForeignKey(
        SingerPodcastModel,
        verbose_name="گوینده",
        on_delete=models.CASCADE,
        related_name="singer",
    )
    kurd_date = models.CharField(verbose_name="تاریخ کردی", max_length=20)
    persian_date = models.CharField(verbose_name="تاریخ فارسی", max_length=20)
    english_date = models.CharField(verbose_name="تاریخ انگلیسی", max_length=20)
    popularity_rate = models.FloatField(verbose_name="میزان محبوبیت", default=0.0)
    music = models.FileField(verbose_name="پادکست", upload_to=file_path, max_length=100)
    writer_kurd = models.CharField(verbose_name="نویسنده کردی", max_length=50)
    writer_persian = models.CharField(verbose_name="نویسنده فارسی", max_length=50)
    writer_english = models.CharField(verbose_name="نویسنده انگلیسی", max_length=50)
    musictext_kurd = models.CharField(verbose_name="موسیقی متن کردی", max_length=50)
    musictext_persian = models.CharField(verbose_name="موسیقی متن فارسی", max_length=50)
    musictext_english = models.CharField(
        verbose_name="موسیقی متن انگلیسی", max_length=50
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=file_path,
        verbose_name="عکس پادکست",
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
        verbose_name = "پادکست"
        verbose_name_plural = "پادکست صوتی"

    def __str__(self):
        return self.name_persian




class PodcastVideoModel(models.Model):
    name_kurd = models.CharField(max_length=100, verbose_name="نام پادکست کردی")
    name_persian = models.CharField(max_length=100, verbose_name="نام پادکست فارسی")
    name_english = models.CharField(max_length=100, verbose_name="نام پادکست انگلیسی")
    category = models.ForeignKey(
        CategoryPodcastModel, verbose_name="دسته", on_delete=models.CASCADE
    )
    singer = models.ForeignKey(
        SingerPodcastModel, verbose_name="گوینده", on_delete=models.CASCADE
    )
    kurd_date = models.CharField(verbose_name="تاریخ کردی", max_length=20)
    persian_date = models.CharField(verbose_name="تاریخ فارسی", max_length=20)
    english_date = models.CharField(verbose_name="تاریخ انگلیسی", max_length=20)
    popularity_rate = models.FloatField(verbose_name="میزان محبوبیت", default=0.0)
    music = models.FileField(verbose_name="پادکست", upload_to=file_path)
    writer_kurd = models.CharField(verbose_name="نویسنده کردی", max_length=50)
    writer_persian = models.CharField(verbose_name="نویسنده فارسی", max_length=50)
    writer_english = models.CharField(verbose_name="نویسنده انگلیسی", max_length=50)
    musictext_kurd = models.CharField(verbose_name="موسیقی متن کردی", max_length=50)
    musictext_persian = models.CharField(verbose_name="موسیقی متن فارسی", max_length=50)
    musictext_english = models.CharField(
        verbose_name="موسیقی متن انگلیسی", max_length=50
    )
    compilation_kurd = models.CharField(verbose_name="تدوین کردی", max_length=50)
    compilation_persian = models.CharField(verbose_name="تدوین فارسی", max_length=50)
    compilation_english = models.CharField(verbose_name="تدوین انگلیسی", max_length=50)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=file_path,
        verbose_name="عکس پادکست",
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
        verbose_name = "پادکست"
        verbose_name_plural = "پادکست صوتی"

    def __str__(self):
        return self.name_persian
