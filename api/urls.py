from django.urls import path, include
from .views import VideoViewSet, UserViewSet, ImageViewSet, VirtualTourViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register('videos', VideoViewSet, basename='videos')
router.register('images', ImageViewSet, basename='images')
router.register('images', VirtualTourViewSet, basename='virtualtours')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
