from django.urls import path
# from . views import video_list, video_details
from .views import VideoList, VideoDetails


urlpatterns = [
    path('videos/', VideoList.as_view()),
    path('videos/<int:id>/', VideoDetails.as_view()),



    # path('videos/', video_list),
    # path('videos/<int:pk>/', video_details),
]
