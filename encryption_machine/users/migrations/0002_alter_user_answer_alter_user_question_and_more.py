# Generated by Django 4.2.1 on 2023-06-23 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answer',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='user',
            name='question',
            field=models.CharField(max_length=100, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=32, verbose_name='token'),
        ),
    ]