from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import QuerySet

from wagtailmedia.models import Media as WagtailMedia


from home import models as home_models

from .models import Exhibition, Room, Media, Image, Wall


class ExhibitionBuilder:

    def build(self, exhibition_id: int):
        exhibition = self._build_exhibition(exhibition_id)

        return exhibition

    def _build_exhibition(self, exhibition_id):
        home_exhibition = QuerySet(home_models.Exhibition)\
            .filter(page_ptr_id=exhibition_id, live=True).first()

        home_rooms = QuerySet(home_models.Room).filter(
            exhibition_page=exhibition_id
        )

        rooms = self._build_rooms(home_rooms)

        exhibition = Exhibition(
            home_exhibition.page_title,
            home_exhibition.strapline,
            home_exhibition.flyer_image_id,
            rooms
        )

        return exhibition

    def _build_rooms(self, home_rooms):
        rooms = []
        for home_room in home_rooms:
            walls = self._build_walls(home_room)

            room = Room(walls)
            rooms.append(room)
        return rooms

    def _build_walls(self, home_room):
        home_walls = QuerySet(home_models.Wall).filter(room_page=home_room.id)
        walls = []
        for home_wall in home_walls:

            images = self._build_images(home_wall)
            media = self._build_media(home_wall)

            wall = Wall(media, images)
            walls.append(wall)

        return walls

    def _build_media(self, home_wall):
        exhibition_media = QuerySet(home_models.ExhibitionMedia) \
            .filter(page_id=home_wall.id)
        exhibition_media_media_ids = [
            exhibition_media.media_id
            for exhibition_media
            in exhibition_media
        ]
        media_list = list(
            WagtailMedia.objects.filter(id__in=exhibition_media_media_ids).values()
        )

        media = []
        for media_item in media_list:
            api_media_item = Media(**media_item)
            media.append(api_media_item)

        return media

    def _build_images(self, home_wall):
        exhibition_images = QuerySet(home_models.ExhibitionImage) \
            .filter(page_id=home_wall.id)
        exhibition_image_image_ids = [
            exhibition_image.image_id
            for exhibition_image
            in exhibition_images
        ]
        wagtail_images_list = list(
            home_models.SoundbiteImage.objects.filter(id__in=exhibition_image_image_ids).values()
        )

        images = []
        for wagtail_image in wagtail_images_list:
            api_images_item = Image(**wagtail_image)
            images.append(api_images_item)

        return images
