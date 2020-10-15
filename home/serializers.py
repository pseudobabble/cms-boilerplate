#!/usr/bin/env python
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import Field, FileField
from rest_framework.serializers import ModelSerializer, FileField

from wagtail.images.api.v2.serializers import ImageSerializer as WagtailImageSerializer


from wagtailmedia.models import Media as WagtailMedia
from home.models import CustomMedia



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


class MediaSerializer(serializers.BaseSerializer):
    blurb = serializers.CharField()
    created_at = serializers.DateTimeField()
    duration = serializers.IntegerField()
    file = serializers.FileField()
    id = serializers.IntegerField()
    title = serializers.CharField()
    type = serializers.CharField()
    uploaded_by_user = UserSerializer()

    def to_internal_value(self, data):
        pass

    def to_representation(self, instance):
        representation = {}
        representation['blurb'] = instance.blurb
        representation['created_at'] = instance.created_at
        representation['duration'] = instance.duration
        representation['file'] = instance.file.url
        representation['id'] = instance.id
        representation['title'] = instance.title
        representation['type'] = instance.type
        representation['uploaded_by_user'] = UserSerializer(instance.uploaded_by_user).data

        return representation

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class SoundbiteImageSerializer(WagtailImageSerializer):
    download_url = MediaDownloadUrlField(read_only=True)
    soundbite = MediaSerializer()
    blurb = serializers.CharField()
    physical_height = serializers.FloatField()
    physical_width = serializers.FloatField()
    uploaded_by_user = UserSerializer()
