# Generated by Django 4.2 on 2023-04-30 13:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smb_base', '0005_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='question_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
