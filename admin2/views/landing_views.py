# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin

from admin2.forms import LandingForm, LandingSeoForm, LandingFormForm
from landing.models import Landing


class LandingMixin(ContextMixin):
    model = None
    def get_context_data(self, **kwargs):
        context = super(LandingMixin, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class LandingList(ListView):
    model = Landing
    template_name = 'admin2/landing/landing_list.html'


class LandingEdit(LandingMixin, UpdateView):
    model = Landing
    template_name = 'admin2/landing/landing_edit.html'
    pk_url_kwarg = 'pk'
    form_class = LandingForm

    def get_success_url(self):
        return reverse_lazy('admin2:landing_edit', args=[self.object.id])


class LandingEditSeo(LandingMixin, UpdateView):
    model = Landing
    template_name = 'admin2/landing/landing_seo.html'
    pk_url_kwarg = 'pk'
    form_class = LandingSeoForm

    def get_success_url(self):
        return reverse_lazy('admin2:landing_edit_seo', args=[self.object.id])


class LandingEditForm(LandingMixin, UpdateView):
    model = Landing
    template_name = 'admin2/landing/landing_form.html'
    pk_url_kwarg = 'pk'
    form_class = LandingFormForm

    def get_success_url(self):
        return reverse_lazy('admin2:landing_edit_form', args=[self.object.id])


class LandingCreate(CreateView):
    model = Landing
    template_name = 'admin2/landing/landing_edit.html'
    form_class = LandingForm

    def get_success_url(self):
        return reverse_lazy('admin2:landing_edit', args=[self.object.id])


class LandingDelete(DeleteView):
    model = Landing
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:landings'))

