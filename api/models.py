from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, default='Description...')
    cover = models.ImageField(upload_to='covers')
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, default='Description...')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
