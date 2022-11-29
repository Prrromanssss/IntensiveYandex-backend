# Generated by Django 3.2.16 on 2022-11-28 19:32

import catalog.validators
import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='Описание должно содержать слова "роскошно" и "превосходно"', validators=[catalog.validators.validate_amazing], verbose_name='описание'),
        ),
    ]
