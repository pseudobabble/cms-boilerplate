#!/usr/bin/env python

from rest_framework.fields import Field, CharField
from rest_framework.serializers import ModelSerializer
from wagtail.api.v2.serializers import BaseSerializer
from wagtail.images.api.v2.serializers import ImageSerializer as WagtailImageSerializer
from wagtail.images.models import Image

from wagtailmedia.models import Media as WagtailMedia

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



class SoundbiteImageSerializer(WagtailImageSerializer):
    download_url = MediaDownloadUrlField(read_only=True)
    soundbite = MediaSerializer()



