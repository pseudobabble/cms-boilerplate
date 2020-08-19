from django.db import models
from django.db.models import TextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock, RichTextBlock

from wagtail.images.blocks import ImageChooserBlock




class HomePage(Page):
    class Meta:
        verbose_name = 'homepage'


    hero_text = TextField(null=True, blank=True)
    hero_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    page_stream = StreamField([
        ('heading', CharBlock()),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('hero_text'),
        FieldPanel('hero_background'),
        StreamFieldPanel('page_stream'),
    ]

    # TODO  19/08/2020 14:58: Implement these properly
    parent_page_types = []
    subpage_types = []


class ExhibitionIndex(Page):
    pass

class Exhibition(Page):
    pass


class WorkshopIndex(Page):
    pass

class Workshop(Page):
    pass


class ArtistIndex(Page):
    pass

class Artist(Page):
    pass


class Mission(Page):
    pass


class Contact(Page):
    pass


