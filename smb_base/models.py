from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from taggit.models import Tag



class Comment(models.Model):
    question = models.ForeignKey(Question, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    content = RichTextUploadingField()
    date_created = models.DateTimeField(default=timezone.now)   
    likes = models.ManyToManyField(User, related_name='comment_post')

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_success_url(self):
        return reverse('smb_base:question-detail', kwargs={'pk':self.pk})
    
    def total_likes(self):
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
