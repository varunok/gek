# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from dal import autocomplete
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms.widgets import TextInput, Textarea, FileInput, Select, SelectMultiple
from ckeditor.widgets import CKEditorWidget
from django.urls import reverse_lazy

from admin2.models import ContactPageModel
from articles.models import Sections, Articles
from common.models import Video, Photo, Advantage, Feed, Schedule
from rieltor_object.models import Building, Ofice, NewBuilding, Daily, Earth
from services.models import ServicesRieltor, Repair, Insurance, Cleaning, InstallationWater, UniversalService


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


class RieltorServiceForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = 'is_enable',
        fields = '__all__'


class ValuationForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = 'is_enable',
        fields = '__all__'


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = 'is_enable',
        fields = '__all__'


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = 'is_enable',
        fields = '__all__'


class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        exclude = 'is_enable',
        fields = '__all__'


class InstallationWaterForm(forms.ModelForm):
    class Meta:
        model = InstallationWater
        exclude = 'is_enable',
        fields = '__all__'


class UniversalServiceForm(forms.ModelForm):
    class Meta:
        model = UniversalService
        exclude = 'is_enable',
        fields = '__all__'


class UniversalServiceCreateForm(forms.ModelForm):
    class Meta:
        model = UniversalService
        exclude = 'is_enable',
        fields = '__all__'


VideoRieltorServiceSet = generic_inlineformset_factory(
    Video,
    can_delete=False,
    extra=2,
    min_num=2,
    max_num=2
)

VideoServiceSet = generic_inlineformset_factory(
    Video,
    can_delete=False,
    extra=1,
    min_num=1,
    max_num=1
)

FeedSet = generic_inlineformset_factory(
    Feed,
    extra=0,
    min_num=1
)

ScheduleSet = generic_inlineformset_factory(
    Schedule,
    extra=0,
    min_num=1
)


FeedVideoSet = generic_inlineformset_factory(
    Video,
    extra=0,
    min_num=1
)


class AdvantageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Фото',

    )
    image.widget.input_text = ''


AdvantageSet = generic_inlineformset_factory(
    Advantage,
    form=AdvantageForm,
    can_delete=False,
    extra=4,
    min_num=4,
    max_num=4,

)


class BuildingEditForm(forms.ModelForm):

    class Meta:
        model = Building
        exclude = ['views']
        fields = '__all__'


class NewBuildingEditForm(forms.ModelForm):

    class Meta:
        model = NewBuilding
        exclude = ['views']
        fields = '__all__'


class OficeEditForm(forms.ModelForm):

    class Meta:
        model = Ofice
        exclude = ['views']
        fields = '__all__'


class EarthEditForm(forms.ModelForm):

    class Meta:
        model = Earth
        fields = '__all__'
        widgets = {
            'communication': autocomplete.Select2Multiple(),
            'structure_house': autocomplete.Select2Multiple(),
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:earth-district-autocomplete'),
            )
        }


class DailyEditForm(forms.ModelForm):

    class Meta:
        model = Daily
        exclude = ['views', 'infrastructures']
        fields = '__all__'
        widgets = {
            'apartment_has': autocomplete.ModelSelect2Multiple(
                url=reverse_lazy('admin2:apartment-has-autocomplete'),
            )
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPageModel
        fields = '__all__'
        widgets = {
            'users': autocomplete.ModelSelect2Multiple(
                url=reverse_lazy('admin2:users-autocomplete'),
            )
        }
