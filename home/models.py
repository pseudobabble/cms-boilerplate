from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField, URLField, ForeignKey
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, \
    InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.api import APIField

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
        'home.SoundbiteImage',
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
        'home.ExhibitionIndex',
        'home.WorkshopIndex',
        'home.ArtistIndex',
        'home.Mission'
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
    strapline = TextField(null=True, blank=True)
    flyer_image = models.ForeignKey(
        'home.SoundbiteImage',
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
        InlinePanel('exhibition_images', label='Exhibition Images')
    ]

    parent_page_types = ['home.ExhibitionIndex']
    subpage_types = ['home.Room']


    api_fields = [
        APIField('page_title'),
        APIField('strapline'),
        APIField('flyer_image'),
    ]


class Room(Page):
    exhibition_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    room_name = TextField(null=True, blank=True)
    strapline = TextField(null=True, blank=True)
    blurb = StreamField([
        ('heading', CharBlock()),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('room_name'),
        FieldPanel('strapline'),
        StreamFieldPanel('blurb'),
        PageChooserPanel('exhibition_page', 'home.Exhibition'),
    ]

    parent_page_types = ['home.Exhibition']
    subpage_types = ['home.Wall']


class Wall(Page):
    room_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    wall_name = TextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('wall_name'),
        MultiFieldPanel(
            [
                InlinePanel('exhibition_images', label='An image'),
                InlinePanel('exhibition_media', label='A video or audio file'),
            ],
            heading='Exhibition Works'
        ),
        PageChooserPanel('room_page', 'home.Room'),
    ]

    parent_page_types = ['home.Room']
    subpage_types = []


class ExhibitionImage(Orderable):
    page = ParentalKey(Wall, related_name='exhibition_images')
    image = models.ForeignKey(
        'home.SoundbiteImage',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        ImageChooserPanel('image'),
    ]


class ExhibitionMedia(Orderable):
    page = ParentalKey(Wall, related_name='exhibition_media')
    media = models.ForeignKey(
        'home.CustomMedia',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        MediaChooserPanel('media'),
    ]


class WorkshopIndex(Page):
    class Meta:
        verbose_name = 'workshops'

    page_title = TextField(null=True, blank=True)
    blurb = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('blurb'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        'home.Workshop'
    ]


class Workshop(Page):
    page_title = TextField(null=True, blank=True)
    strapline = TextField(null=True, blank=True)
    page_stream = StreamField([
        ('heading', CharBlock()),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('strapline'),
        StreamFieldPanel('page_stream'),
        InlinePanel('workshop_images', label='Workshop Images')
    ]

    parent_page_types = ['home.WorkshopIndex']
    subpage_types = []


class WorkshopImage(Orderable):
    page = ParentalKey(Workshop, related_name='workshop_images')
    image = models.ForeignKey(
        'home.SoundbiteImage',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        ImageChooserPanel('image')
    ]


class ArtistIndex(Page):
    class Meta:
        verbose_name = 'artists'

    page_title = TextField(null=True, blank=True)
    blurb = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('blurb'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        'home.Artist'
    ]

class Artist(Page):
    name = TextField(null=True, blank=True)
    photo = models.ForeignKey(
        'home.SoundbiteImage',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )
    blurb = RichTextField(null=True, blank=True)
    portfolio_link = URLField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        ImageChooserPanel('photo'),
        FieldPanel('blurb'),
        FieldPanel('portfolio_link'),
        MultiFieldPanel([
            InlinePanel('portfolio_images', label='Portfolio Images'),
            InlinePanel('portfolio_media', label='Portfolio Media')
        ], heading='Display Portfolio')
    ]

    parent_page_types = ['home.ArtistIndex']
    subpage_types = []


class ArtistImage(Orderable):
    page = ParentalKey(Artist, related_name='portfolio_images')
    image = models.ForeignKey(
        'home.SoundbiteImage',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        ImageChooserPanel('image')
    ]


class ArtistMedia(Orderable):
    page = ParentalKey(Artist, related_name='portfolio_media')
    media = models.ForeignKey(
        'wagtailmedia.Media',
        on_delete=models.SET_NULL, related_name='+',
        null=True,
        blank=True
    )

    panels = [
        ImageChooserPanel('media')
    ]



class Mission(Page):
    page_title = TextField(null=True, blank=True)
    page_stream = StreamField([
        ('heading', CharBlock()),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        StreamFieldPanel('page_stream'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []


class Contact(Page):
    pass


