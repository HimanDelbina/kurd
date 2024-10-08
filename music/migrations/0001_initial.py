# Generated by Django 5.0.6 on 2024-06-16 10:20

import django.db.models.deletion
import music.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMusicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام دسته بندی کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام دسته بندی فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام دسته بندی انگلیسی')),
            ],
            options={
                'verbose_name': 'نام دسته بندی',
                'verbose_name_plural': 'نام دسته بندی',
            },
        ),
        migrations.CreateModel(
            name='SingerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام خواننده کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام خواننده فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام خواننده انگلیسی')),
            ],
            options={
                'verbose_name': 'نام خواننده',
                'verbose_name_plural': 'نام خواننده',
            },
        ),
        migrations.CreateModel(
            name='MusicVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام موزیک کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام موزیک فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام موزیک انگلیسی')),
                ('kurd_date', models.CharField(max_length=20, verbose_name='تاریخ کردی')),
                ('persian_date', models.CharField(max_length=20, verbose_name='تاریخ فارسی')),
                ('english_date', models.CharField(max_length=20, verbose_name='تاریخ انگلیسی')),
                ('popularity_rate', models.FloatField(default=0.0, verbose_name='میزان محبوبیت')),
                ('music', models.FileField(max_length=1000, upload_to=music.models.file_path, verbose_name='موزیک')),
                ('image', models.ImageField(blank=True, null=True, upload_to=music.models.file_path, verbose_name='عکس موزیک')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.categorymusicmodel', verbose_name='دسته')),
                ('signer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.singermodel', verbose_name='خواننده')),
            ],
            options={
                'verbose_name': 'موزیک',
                'verbose_name_plural': 'موزیک ها',
            },
        ),
        migrations.CreateModel(
            name='MusicMp3Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kurd', models.CharField(max_length=100, verbose_name='نام موزیک کردی')),
                ('name_persian', models.CharField(max_length=100, verbose_name='نام موزیک فارسی')),
                ('name_english', models.CharField(max_length=100, verbose_name='نام موزیک انگلیسی')),
                ('kurd_date', models.CharField(max_length=20, verbose_name='تاریخ کردی')),
                ('persian_date', models.CharField(max_length=20, verbose_name='تاریخ فارسی')),
                ('english_date', models.CharField(max_length=20, verbose_name='تاریخ انگلیسی')),
                ('popularity_rate', models.FloatField(default=0.0, verbose_name='میزان محبوبیت')),
                ('music', models.FileField(upload_to=music.models.file_path, verbose_name='موزیک')),
                ('image', models.ImageField(blank=True, null=True, upload_to=music.models.file_path, verbose_name='عکس موزیک')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.categorymusicmodel', verbose_name='دسته')),
                ('signer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.singermodel', verbose_name='خواننده')),
            ],
            options={
                'verbose_name': 'موزیک',
                'verbose_name_plural': 'موزیک ها',
            },
        ),
    ]
