from django.contrib.auth.models import User
from django.db import models
from django.http import request

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length = 150)
    video = models.FileField(upload_to='video/%y')

    def __str__(self):
        return self.caption
