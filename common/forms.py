# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import modelformset_factory

from common.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

ImageFormSet = modelformset_factory(Photo, form=PhotoForm, extra=3)