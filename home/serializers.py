#!/usr/bin/env python

from rest_framework.fields import Field
from wagtail.api.v2.serializers import BaseSerializer
from wagtail.images.api.v2.serializers import ImageSerializer as WagtailImageSerializer
from wagtail.images.models import Image

from home.models import SoundbiteImage


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


class MediaSerializer(BaseSerializer):
    download_url = MediaDownloadUrlField(read_only=True)
    artist = ArtistField(read_only=True)


class ImageSerializer(WagtailImageSerializer):
    artist = ArtistField(read_only=True)


class SoundbiteImageSerializer(WagtailImageSerializer):
    class Meta:
        model = SoundbiteImage
        fields = '__all__'



