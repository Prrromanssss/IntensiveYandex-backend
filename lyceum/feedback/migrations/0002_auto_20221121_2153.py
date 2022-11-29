# Generated by Django 3.2.16 on 2022-11-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='mail',
            field=models.EmailField(default='1@example.com', help_text='Почта пользователя', max_length=254, verbose_name='почта'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='', help_text='Имя пользователя', max_length=150, verbose_name='имя'),
        ),
    ]