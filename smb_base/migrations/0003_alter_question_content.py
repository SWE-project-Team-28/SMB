# Generated by Django 4.2 on 2023-04-29 15:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smb_base', '0002_question_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
