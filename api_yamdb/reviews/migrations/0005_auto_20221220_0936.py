# Generated by Django 3.2 on 2022-12-20 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Допустимы значения от 1 до 10'), django.core.validators.MaxValueValidator(10, 'Допустимы значения от 1 до 10')], verbose_name='Рейтинг'),
        ),
    ]
