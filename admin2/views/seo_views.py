# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from common.mixins import SuccesMixin, MessageMixin
from seo.models import SEO


class SEOList(LoginRequiredMixin, ListView):
    model = SEO
    paginate_by = 10
    template_name = 'admin2/seo/seo_list.html'


class SeoCreate(LoginRequiredMixin, SuccesMixin, MessageMixin, CreateView):
    model = SEO
    template_name = 'admin2/seo/seo_detail.html'
    fields = '__all__'


class SEOEdit(LoginRequiredMixin, SuccesMixin, MessageMixin, UpdateView):
    model = SEO
    template_name = 'admin2/seo/seo_detail.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(SEOEdit, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class SeoDelete(LoginRequiredMixin, DeleteView):
    model = SEO
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:seo')


