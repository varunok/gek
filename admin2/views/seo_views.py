# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from seo.models import SEO


class SEOList(ListView):
    model = SEO
    template_name = 'admin2/seo/seo_list.html'


class SeoCreate(CreateView):
    model = SEO
    template_name = 'admin2/seo/seo_detail.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:seo_edit', args=[self.object.id])


class SEOEdit(UpdateView):
    model = SEO
    template_name = 'admin2/seo/seo_detail.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('admin2:seo_edit', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super(SEOEdit, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class SeoDelete(DeleteView):
    model = SEO
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:seo'))

