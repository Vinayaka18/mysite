from django.db import models

# Create your models here.
# yourappname/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need
    pass


class Try(models.Model):
    image = models.ImageField(upload_to='media/videos/')


class HtmlVideo(models.Model):
    title = models.CharField(max_length=255)
    video_source = models.FileField(upload_to='media/videos/')
    thumbnail_image = models.ImageField(upload_to='media/thumbnails/')
    