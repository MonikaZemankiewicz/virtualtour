from django.contrib import admin
from .models import Video, Image
# Register your models here.

# admin.site.register(Video)


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')


@admin.register(Image)
class ImageModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
