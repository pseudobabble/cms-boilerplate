#!/usr/bin/env python
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer

from wagtail.images.api.v2.serializers import ImageSerializer as WagtailImageSerializer

from wagtailmedia.models import Media as WagtailMedia


class MediaDownloadUrlField(Field):
    """
    Serializes the "download_url" field for Media.

    Example:
    "download_url": "/media/media/a_test_Media.jpg"
    """
    def get_attribute(self, instance):
        return instance

    def to_representation(self, media):
        return media.file.url

class ImageDownloadUrlField(Field):
    """
    Serializes the "download_url" field for Media.

    Example:
    "download_url": "/media/media/a_test_Media.jpg"
    """
    def get_attribute(self, instance):
        return instance

    def to_representation(self, image):
        return image.file.url

class ArtistField(Field):
    """
    Serializes the "download_url" field for Media.

    Example:
    "download_url": "/media/media/a_test_Media.jpg"
    """
    def get_attribute(self, instance):
        return instance

    def to_representation(self, model):
        return '{} {}'.format(model.uploaded_by_user.first_name, model.uploaded_by_user.last_name)


class MediaSerializer(ModelSerializer):
    class Meta:
        model = WagtailMedia
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'groups',
            'id',
            'username'
        ]


class SoundbiteImageSerializer(WagtailImageSerializer):
    download_url = MediaDownloadUrlField(read_only=True)
    soundbite = MediaSerializer()
    blurb = serializers.CharField()
    physical_height = serializers.FloatField()
    physical_width = serializers.FloatField()
    uploaded_by_user = UserSerializer()
