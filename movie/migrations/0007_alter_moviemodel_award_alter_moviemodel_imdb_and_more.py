# Generated by Django 5.0.6 on 2024-06-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_awardsmodel_moviemodel_award'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='award',
            field=models.ManyToManyField(blank=True, null=True, to='movie.awardsmodel', verbose_name='جایزه ها '),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='imdb',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='نمره imdb'),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='popularity_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='میزان محبوبیت'),
        ),
    ]
