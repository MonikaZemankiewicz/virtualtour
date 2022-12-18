from django.contrib import admin
from .models import Video
# Register your models here.

# admin.site.register(Video)


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
