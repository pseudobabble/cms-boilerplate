#!/usr/bin/env python
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from exhibition.builders import ExhibitionBuilder
from exhibition.serializers import ExhibitionSerializer


class ExhibitionViewSet(ViewSet):
    serializer_class = ExhibitionSerializer

    def retrieve(self, request, pk=None):
        exhibition_id = pk

        exhibition_builder = ExhibitionBuilder()
        exhibition = exhibition_builder.build(exhibition_id)
        serializer = ExhibitionSerializer(instance=exhibition)
        return Response(serializer.data)

