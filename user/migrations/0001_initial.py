# Generated by Django 5.0.6 on 2024-06-15 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name=' نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('password', models.CharField(max_length=20, verbose_name='رمز')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='MyOwnToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('userTokens', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='user.usermodel', verbose_name='user_token')),
            ],
            options={
                'verbose_name': 'Users Token',
                'verbose_name_plural': 'User Token',
            },
        ),
    ]
