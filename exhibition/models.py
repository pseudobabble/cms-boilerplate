from datetime import datetime
from typing import List, Any, Union

from django.contrib.auth.models import User
from wagtail.core.models import Collection

from wagtailmedia.models import Media as WagtailMedia


class Image:
    def __init__(
            self,
            id: Union[int, None],
            collection_id: Union[int, None],
            file: Union[str, None],
            file_hash: Union[str, None],
            file_size: Union[int, None],
            focal_point_height: Union[int, None],
            focal_point_width: Union[int, None],
            focal_point_x: Union[int, None],
            focal_point_y: Union[int, None],
            height: Union[int, None],
            width: Union[int, None],
            title: Union[str, None],
            uploaded_by_user_id: Union[int, None],
            created_at: datetime,
            soundbite_id: Union[int, None],
            blurb: Union[str, None],
            physical_height: Union[int, None],
            physical_width: Union[int, None],
    ):
        self.physical_width = physical_width
        self.physical_height = physical_height
        self.blurb = blurb
        self.id = id
        self.soundbite = WagtailMedia.objects.filter(pk=soundbite_id).first()
        self.uploaded_by_user = User.objects.get(pk=uploaded_by_user_id)
        self.title = title
        self.width = width
        self.height = height
        self.focal_point_y = focal_point_y
        self.focal_point_x = focal_point_x
        self.focal_point_height = focal_point_height
        self.focal_point_width = focal_point_width
        self.file_size = file_size
        self.file_hash = file_hash
        self.file = file
        self.created_at = created_at
        self.collection = Collection.objects.get(pk=collection_id)


class Media:
    def __init__(
            self,
            id: Union[int, None],
            collection_id: Union[int, None],
            created_at: Union[datetime, None],
            duration: Union[int, None],
            file: Union[str, None],
            height: Union[int, None],
            thumbnail: Union[str, None],
            title: Union[str, None],
            type: Union[str, None],
            uploaded_by_user_id: Union[int, None],
            width: Union[int, None]
     ):
        self.width = width
        self.uploaded_by_user = User.objects.get(pk=uploaded_by_user_id)
        self.type = type
        self.title = title
        self.thumbnail = thumbnail
        self.id = id
        self.height = height
        self.file = file
        self.duration = duration
        self.created_at = created_at
        self.collection = Collection.objects.get(pk=collection_id)


class Wall:
    def __init__(self, media: List[Media], images: List[Image]):
        self.media = media
        self.images = images


Walls = List[Wall]


class Room:
    def __init__(self, walls: Walls):
        self.walls = walls


RoomList = List[Room]


class Exhibition:
    def __init__(
            self,
            page_title: str,
            strapline: str,
            flyer_image: int,
            rooms: RoomList
    ):
        self.page_title = page_title
        self.strapline = strapline
        self.flyer_image = flyer_image
        self.rooms = rooms
