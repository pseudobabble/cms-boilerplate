#!/usr/bin/env python
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet

from home.models import SoundbiteImage, CustomMedia
from home.serializers import MediaSerializer, SoundbiteImageSerializer


class MediaAPIViewSet(BaseAPIViewSet):
    base_serializer_class = MediaSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + [
        'title',
        'width',
        'height',
    ]
    meta_fields = BaseAPIViewSet.meta_fields + ['tags', 'artist']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'tags']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['title']
    name = 'media'
    model = CustomMedia


class ImagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = SoundbiteImageSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + [
        'title',
        'width',
        'height',
        'soundbite',
        'file',
        'blurb',
        'physical_height',
        'physical_width',
        'uploaded_by_user'
    ]
    meta_fields = BaseAPIViewSet.meta_fields + ['tags']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'tags']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['title']
    name = 'images'
    model = SoundbiteImage
