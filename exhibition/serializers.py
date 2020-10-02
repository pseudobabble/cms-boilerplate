from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import fields


from wagtail.core.models import Collection
from wagtail.images.api.v2.serializers import ImageSerializer as WagtailImageSerializer

from home.serializers import SoundbiteImageSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class MediaSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()
    duration = serializers.IntegerField()
    file = serializers.CharField()
    height = serializers.IntegerField()
    id = serializers.IntegerField()
    thumbnail = serializers.CharField()
    title = serializers.CharField()
    uploaded_by_user = UserSerializer()
    width = serializers.IntegerField()
    type = serializers.CharField()


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    file = serializers.CharField()
    file_size = serializers.IntegerField()
    focal_point_height = serializers.IntegerField()
    focal_point_width = serializers.IntegerField()
    focal_point_x = serializers.IntegerField()
    focal_point_y = serializers.IntegerField()
    height = serializers.IntegerField()
    width = serializers.IntegerField()
    title = serializers.CharField()
    soundbite = MediaSerializer()
    uploaded_by_user = UserSerializer()


class RoomSerializer(serializers.Serializer):
    media = MediaSerializer(many=True)
    images = ImageSerializer(many=True)

class ExhibitionSerializer(serializers.Serializer):
    page_title = fields.CharField()
    strapline  = fields.CharField()
    # flyer_image = SoundbiteImageSerializer() #  << IT WAS THIS
    rooms = RoomSerializer(many=True)


