#!/usr/bin/env python
from django import forms
from django.forms import FloatField
from wagtail.images.forms import BaseImageForm
from wagtailmedia.forms import BaseMediaForm
from .models import CustomMedia

class CustomMediaForm(BaseMediaForm):
    # class Meta:
    #     widgets = {
    #         'tags': widgets.AdminTagWidget,
    #         'file': forms.FileInput,
    #         'thumbnail': forms.ClearableFileInput,
    #         'blurb': forms.CharField
    #     }
    blurb = forms.CharField()


class SoundbiteImageForm(BaseImageForm):
    soundbite = forms.ModelChoiceField(queryset=CustomMedia.objects.all())

# TODO  15/10/2020 12:05: custom form for ExhibitionImage?
