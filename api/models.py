from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, default='Description...')

    def __str__(self):
        return self.title
