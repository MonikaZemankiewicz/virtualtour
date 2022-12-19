from django.urls import path, include
from .views import VideoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


# from . views import video_list, video_details
# from .views import VideoList, VideoDetails

router = DefaultRouter()
router.register('videos', VideoViewSet, basename='videos')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),



]
