# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.views.generic.base import ContextMixin

from admin2.forms import DownBannersImageForm, SideBannersImageForm, DownBannersCodeForm, SideBannersCodeForm
from banners.models import DownBanner, SideBanner
from common.mixins import MessageMixin


class BannersMixin(ContextMixin):
    model = None

    def get_object(self, queryset=None):
        return self.model.get_solo()

    def get_context_data(self, **kwargs):
        context = super(BannersMixin, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class Banners(TemplateView):
    template_name = 'admin2/banners/banners_list.html'

    def get_context_data(self, **kwargs):
        context = super(Banners, self).get_context_data(**kwargs)
        context['downbanner'] = DownBanner.get_solo()
        context['sidebanner'] = SideBanner.get_solo()
        return context


class EditBannerImage(BannersMixin, MessageMixin, UpdateView):
    template_name = 'admin2/banners/banners_image_edit.html'

    def get_form_class(self):
        object = self.model.__name__.lower()
        if object == 'downbanner':
            return DownBannersImageForm
        elif object == 'sidebanner':
            return SideBannersImageForm

    def get_success_url(self):
        object = self.model.__name__.lower()
        succes_url = reverse_lazy('admin2:{0}s_image'.format(object))
        return succes_url


class EditBannerCode(BannersMixin, MessageMixin, UpdateView):
    template_name = 'admin2/banners/banners_code_edit.html'

    def get_form_class(self):
        object = self.model.__name__.lower()
        if object == 'downbanner':
            return DownBannersCodeForm
        elif object == 'sidebanner':
            return SideBannersCodeForm

    def get_success_url(self):
        object = self.model.__name__.lower()
        succes_url = reverse_lazy('admin2:{0}s_code'.format(object))
        return succes_url