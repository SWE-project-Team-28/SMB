# Generated by Django 3.2.8 on 2021-10-11 22:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0004_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
