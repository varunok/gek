# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.widgets import TextInput, Textarea
from ckeditor.widgets import CKEditorWidget

from articles.models import Sections, Articles


class SectionUpdateForm(forms.ModelForm):

    class Meta:
        model = Sections
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'slug': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'title': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'keywords': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'description': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'heading': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'content': CKEditorWidget(attrs={'class': 'form-control col-md-7 col-xs-12'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data["slug"]
        if Sections.objects.filter(slug=slug).exists():
            raise forms.ValidationError("такой URL уже используется.")
        return slug


class ArticlesUpdateForm(forms.ModelForm):
    views = forms.IntegerField(required=False)

    class Meta:
        model = Articles
        fields = '__all__'