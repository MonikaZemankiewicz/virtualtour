from django.urls import path, include
from .views import VideoViewSet
from rest_framework.routers import DefaultRouter

# from . views import video_list, video_details
# from .views import VideoList, VideoDetails

router = DefaultRouter()
router.register('videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('', include(router.urls)),


    # path('videos/', VideoList.as_view()),
    # path('videos/<int:id>/', VideoDetails.as_view()),
    # path('videos/', video_list),
    # path('videos/<int:pk>/', video_details),
]
