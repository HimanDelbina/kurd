# Generated by Django 5.0.6 on 2024-06-20 07:05

import django.db.models.deletion
import myshow.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام بازیگر کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام بازیگر فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام بازیگر انگلیسی')),
            ],
            options={
                'verbose_name': 'نام بازیگران',
                'verbose_name_plural': 'نام بازیگران',
            },
        ),
        migrations.CreateModel(
            name='AwardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام جایزه کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام جایزه فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام جایزه انگلیسی')),
            ],
            options={
                'verbose_name': 'جایزه ها ',
                'verbose_name_plural': 'جایزه ها ',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام دسته کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام دسته فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام دسته انگلیسی')),
            ],
            options={
                'verbose_name': 'دسته ها ',
                'verbose_name_plural': 'دسته ها ',
            },
        ),
        migrations.CreateModel(
            name='DirectorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام کارگردان کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام کارگردان فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام کارگردان انگلیسی')),
            ],
            options={
                'verbose_name': 'کارگردان',
                'verbose_name_plural': 'کارگردان',
            },
        ),
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام ژانر کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام ژانر فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام ژانر انگلیسی')),
            ],
            options={
                'verbose_name': 'ژانر',
                'verbose_name_plural': 'ژانر',
            },
        ),
        migrations.CreateModel(
            name='ProducerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام تهیه کننده کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام تهیه کننده فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام تهیه کننده انگلیسی')),
            ],
            options={
                'verbose_name': 'تهیه کننده ها ',
                'verbose_name_plural': 'تهیه کننده ها ',
            },
        ),
        migrations.CreateModel(
            name='MyShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام فیلم کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام فیلم فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام فیلم انگلیسی')),
                ('kurd_date', models.CharField(max_length=20, verbose_name='تاریخ کردی')),
                ('persian_date', models.CharField(max_length=20, verbose_name='تاریخ فارسی')),
                ('english_date', models.CharField(max_length=20, verbose_name='تاریخ انگلیسی')),
                ('kurd_description', models.TextField(verbose_name='خلاصه فیلم کردی')),
                ('persian_description', models.TextField(verbose_name='خلاصه فیلم فارسی')),
                ('english_description', models.TextField(verbose_name='خلاصه فیلم انگلیسی')),
                ('imdb', models.CharField(blank=True, max_length=5, null=True, verbose_name='نمره imdb')),
                ('popularity_rate', models.FloatField(blank=True, null=True, verbose_name='میزان محبوبیت')),
                ('movie', models.FileField(max_length=2000, upload_to=myshow.models.file_path, verbose_name='فیلم')),
                ('image', models.ImageField(blank=True, null=True, upload_to=myshow.models.file_path, verbose_name='عکس فیلم')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('actor', models.ManyToManyField(to='myshow.actormodel', verbose_name='نام بازیگران')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshow.categorymodel', verbose_name='دسته')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshow.directormodel', verbose_name='کارگردان')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshow.genremodel', verbose_name='ژانر')),
                ('producer', models.ManyToManyField(to='myshow.producermodel', verbose_name='تهیه کننده ها ')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم ها',
            },
        ),
    ]
