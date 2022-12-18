from django.urls import path
from . views import video_list, video_details


urlpatterns = [
    path('videos/', video_list),
    path('videos/<int:pk>/', video_details),
]
