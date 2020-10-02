#!/usr/bin/env python
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.images.models import Image
from wagtailmedia.models import Media

from home.serializers import MediaSerializer, SoundbiteImageSerializer


class MediaAPIViewSet(BaseAPIViewSet):
    base_serializer_class = MediaSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + ['title', 'width', 'height']
    meta_fields = BaseAPIViewSet.meta_fields + ['tags', 'download_url', 'artist']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'tags', 'download_url', 'artist']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['title', 'download_url', 'artist']
    name = 'media'
    model = Media


class ImagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = SoundbiteImageSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + ['title', 'width', 'height']
    meta_fields = BaseAPIViewSet.meta_fields + ['tags', 'download_url', 'artist']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'tags', 'download_url', 'artist']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['title', 'download_url', 'artist']
    name = 'images'
    model = SoundbiteImageSerializer
