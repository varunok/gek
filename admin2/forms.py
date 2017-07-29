# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django import forms
from dal import autocomplete
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.forms.widgets import TextInput, Textarea, FileInput, Select, SelectMultiple, TimeInput
from ckeditor.widgets import CKEditorWidget
from django.urls import reverse_lazy

from admin2.models import ContactPageModel, ActiveFranchise, Notes
from articles.models import Sections, Articles
from banners.models import DownBanner, SideBanner
from common.models import Video, Photo, Advantage, Feed, Schedule, WhatYouKnown, Preparation, Process, Finish
from landing.models import Landing, LandingFutor
from polls.models import Question, Choice, Polls
from rieltor_object.models import Building, Ofice, NewBuilding, Daily, Earth, District
from services.models import ServicesRieltor, Repair, Insurance, Cleaning, InstallationWater, UniversalService, Partner
from videos.models import Videos


class SectionUpdateForm(forms.ModelForm):

    class Meta:
        model = Sections
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'slug': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'title': TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'keywords': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'description': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'heading': Textarea(attrs={'class': 'form-control col-md-7 col-xs-12', 'rows': '5'}),
            'content': CKEditorWidget(attrs={'class': 'form-control col-md-7 col-xs-12'}),
        }


class ArticlesUpdateForm(forms.ModelForm):
    views = forms.IntegerField(required=False)

    class Meta:
        model = Articles
        fields = '__all__'


class RieltorServiceForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class RieltorServiceSEOForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = 'is_enable',
        fields = '__all__'


class ValuationForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class ValuationSEOForm(forms.ModelForm):
    class Meta:
        model = ServicesRieltor
        exclude = ('is_enable',)
        fields = '__all__'


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class RepairSEOForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = 'is_enable',
        fields = '__all__'


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class InsuranceSEOForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = 'is_enable',
        fields = '__all__'


class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class CleaningSEOForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        exclude = 'is_enable',
        fields = '__all__'


class InstallationWaterForm(forms.ModelForm):
    class Meta:
        model = InstallationWater
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo')
        fields = '__all__'


class InstallationWaterSEOForm(forms.ModelForm):
    class Meta:
        model = InstallationWater
        exclude = 'is_enable',
        fields = '__all__'


class UniversalServiceForm(forms.ModelForm):
    class Meta:
        model = UniversalService
        exclude = ('is_enable', 'title_seo', 'SEOTitle', 'SEOKeywords', 'SEODescription', 'content', 'image_seo',
                   'partners', 'base_packet', 'midle_packet', 'expert_packet', 'packet_enable')
        fields = '__all__'


class UniversalServiceSEOForm(forms.ModelForm):
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

WhatYouKnownSet = generic_inlineformset_factory(
    WhatYouKnown,
    extra=0,
    min_num=1
)

PreparationsSet = generic_inlineformset_factory(
    Preparation,
    extra=0,
    min_num=1
)

ProcessSet = generic_inlineformset_factory(
    Process,
    extra=0,
    min_num=1
)

FinishSet = generic_inlineformset_factory(
    Finish,
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
    extra=4,
    min_num=4,
    max_num=4,

)


class BuildingEditForm(forms.ModelForm):

    class Meta:
        model = Building
        exclude = ['views']
        fields = '__all__'
        widgets = {
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:district-autocomplete'),
            ),
            'name': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:name-autocomplete'),
            ),
            'phone': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:phone-autocomplete'),
            )
        }


class NewBuildingEditForm(forms.ModelForm):

    class Meta:
        model = NewBuilding
        exclude = ['views']
        fields = '__all__'
        widgets = {
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:district-autocomplete'),
            ),
            'name': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:name-autocomplete'),
            ),
            'phone': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:phone-autocomplete'),
            )
        }


class OficeEditForm(forms.ModelForm):

    class Meta:
        model = Ofice
        exclude = ['views']
        fields = '__all__'
        widgets = {
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:district-autocomplete'),
            ),
            'name': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:name-autocomplete'),
            ),
            'phone': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:phone-autocomplete'),
            )
        }


class EarthEditForm(forms.ModelForm):

    class Meta:
        model = Earth
        fields = '__all__'
        widgets = {
            'communication': autocomplete.Select2Multiple(),
            'structure_house': autocomplete.Select2Multiple(),
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:earth-district-autocomplete'),
            ),
            'name': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:name-autocomplete'),
            ),
            'phone': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:phone-autocomplete'),
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
            ),
            'district': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:daily-district-autocomplete'),
            ),
            'name': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:name-autocomplete'),
            ),
            'phone': autocomplete.ModelSelect2(
                url=reverse_lazy('admin2:phone-autocomplete'),
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


class VideosCreateForm(forms.ModelForm):
    class Meta:
        model = Videos
        exclude = ['views']
        fields = '__all__'
        widgets = {
            'time': TimeInput()
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ChoicesForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = 'question',
        fields = '__all__'


class PollsForm(forms.ModelForm):
    class Meta:
        model = Polls
        exclude = 'test_end', 'questions', 'results',
        fields = '__all__'


class DownBannersImageForm(forms.ModelForm):
    class Meta:
        model = DownBanner
        exclude = 'code', 'active_code'
        fields = '__all__'

    def save(self, commit=True):
        self.instance.active_code = False
        return super(DownBannersImageForm, self).save(commit=True)


class SideBannersImageForm(forms.ModelForm):
    class Meta:
        model = SideBanner
        exclude = 'code', 'active_code'
        fields = '__all__'

    def save(self, commit=True):
        self.instance.active_code = False
        return super(SideBannersImageForm, self).save(commit=True)


class DownBannersCodeForm(forms.ModelForm):
    class Meta:
        model = DownBanner
        exclude = 'image', 'link'
        fields = '__all__'

    def save(self, commit=True):
        self.instance.active_code = True
        return super(DownBannersCodeForm, self).save(commit=True)


class SideBannersCodeForm(forms.ModelForm):
    class Meta:
        model = SideBanner
        exclude = 'image', 'link'
        fields = '__all__'

    def save(self, commit=True):
        self.instance.active_code = True
        return super(SideBannersCodeForm, self).save(commit=True)


class RedirectForm(forms.ModelForm):
    class Meta:
        model = Redirect
        exclude = 'site',
        fields = '__all__'


class LandingForm(forms.ModelForm):
    district = forms.ModelChoiceField(
        queryset=District.objects,
        empty_label='Все',
        label='Район',
        required=False
    )

    class Meta:
        model = Landing
        exclude = ('SEOTitle', 'SEODescription', 'SEOKeywords', 'title_seo', 'content', 'image_seo', 'image_form',
                   'subtitle_form', 'title_form')
        fields = '__all__'
        widgets = {
            'type_property': autocomplete.Select2Multiple(),
        }


class LandingSeoForm(forms.ModelForm):
    class Meta:
        model = Landing
        exclude = ('slug', 'title', 'type_deal', 'price_gt', 'price_lt', 'footage_gt', 'footage_lt',
                   'rooms', 'district', 'image', 'type_property', 'subtitle_form', 'title_form', 'image_form')
        fields = '__all__'


class LandingFormForm(forms.ModelForm):
    class Meta:
        model = Landing
        exclude = ('slug', 'title', 'type_deal', 'price_gt', 'price_lt', 'footage_gt', 'footage_lt',
                   'rooms', 'district', 'image', 'type_property', 'SEOTitle', 'SEODescription', 'SEOKeywords',
                   'title_seo', 'content', 'image_seo')
        fields = '__all__'


class SettingFranchiseAddForm(forms.ModelForm):
    add_date = forms.IntegerField(
        label='Добавить дней'
    )
    active_franchise = forms.DateField(
        disabled=True,
        label='Франшиза активна до'
    )

    class Meta:
        model = ActiveFranchise
        fields = '__all__'

    def save(self, commit=True):
        self.instance.active_franchise += datetime.timedelta(days=self.cleaned_data['add_date'])
        return super(SettingFranchiseAddForm, self).save(commit=True)


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        exclude = ('is_phone_confirmed', 'application_count',)
        fields = '__all__'


class LandingAddForm(forms.ModelForm):
    class Meta:
        model = LandingFutor
        fields = '__all__'

    def clean_landing(self):
        data = self.cleaned_data['landing']
        if self._meta.model.objects.filter(landing=data).exists():
            raise forms.ValidationError('Уже в списке')
        return data


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'