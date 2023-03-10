from rest_framework import serializers
from .models import Video, Image, VirtualTour
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class VideoSerializer(serializers.ModelSerializer):

    # tags = TagListSerializerField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'image', 'video', 'owner']


class ImageSerializer(serializers.ModelSerializer):

    # tags = TagListSerializerField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'image', 'owner']


class VirtualTourSerializer(serializers.ModelSerializer):

    # tags = TagListSerializerField()

    class Meta:
        model = VirtualTour
        fields = ['id', 'title', 'description', 'image', 'owner', 'link']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        # hide password
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    # override create method to hash the user password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
