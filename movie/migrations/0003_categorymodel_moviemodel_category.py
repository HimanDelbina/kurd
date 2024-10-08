# Generated by Django 5.0.6 on 2024-06-15 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_moviemodel_image'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='moviemodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movie.categorymodel', verbose_name='دسته'),
            preserve_default=False,
        ),
    ]
