from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='covers')
    video = models.TextField()
    owner = models.CharField(max_length=200)
    # video = models.FileField(upload_to='videos')
    # tags = TaggableManager()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, default='Description...')
    image = models.ImageField(upload_to='images')
    owner = models.CharField(max_length=200)
    # tags = TaggableManager()

    def __str__(self):
        return self.title


class VirtualTour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, default='Description...')
    image = models.ImageField(upload_to='images')
    owner = models.CharField(max_length=200)
    link = models.CharField(max_length=255)
    # tags = TaggableManager()

    def __str__(self):
        return self.title
