from django.db import models
from django.db.models import TextField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.blocks import CharBlock, RichTextBlock

from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


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
        ImageChooserPanel('hero_background'),
        StreamFieldPanel('page_stream'),
    ]

    parent_page_types = []
    subpage_types = [
        'home.ExhibitionIndex'
    ]


class ExhibitionIndex(Page):
    class Meta:
        verbose_name = 'exhibitions'

    page_title = TextField(null=True, blank=True)
    blurb = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('blurb'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        'home.Exhibition'
    ]

class Exhibition(Page):
    page_title = TextField(null=True, blank=True)
    strapline =  TextField(null=True, blank=True)
    flyer_image = models.ForeignKey(
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
        FieldPanel('page_title'),
        FieldPanel('strapline'),
        ImageChooserPanel('flyer_image'),
        StreamFieldPanel('page_stream'),
        InlinePanel('exhibition_images')
    ]


class ExhibitionImage(Orderable):
    page = ParentalKey(Exhibition, related_name='exhibition_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        ImageChooserPanel('image')
    ]

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


