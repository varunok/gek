# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin

from admin2.forms import LandingForm, LandingSeoForm, LandingFormForm, LandingAddForm
from common.mixins import MessageMixin, SuccesMixin
from landing.models import Landing, LandingFutor


class LandingMixin(LoginRequiredMixin, MessageMixin, ContextMixin):
    model = None
    def get_context_data(self, **kwargs):
        context = super(LandingMixin, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context


class LandingList(LoginRequiredMixin, ListView):
    model = Landing
    paginate_by = 10
    template_name = 'admin2/landing/landing_list.html'


class LandingEdit(SuccesMixin, LandingMixin, UpdateView):
    model = Landing
    template_name = 'admin2/landing/landing_edit.html'
    pk_url_kwarg = 'pk'
    form_class = LandingForm


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


class LandingCreate(LoginRequiredMixin, SuccesMixin, CreateView):
    model = Landing
    template_name = 'admin2/landing/landing_edit.html'
    form_class = LandingForm


class LandingDelete(LoginRequiredMixin, DeleteView):
    model = Landing
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:landings')


class LandingFutorList(LoginRequiredMixin, ListView):
    model = LandingFutor
    template_name = 'admin2/landing/landing_futor_list.html'
    paginate_by = 10


class LandingFutorAdd(LoginRequiredMixin, CreateView):
    model = LandingFutor
    template_name = 'admin2/landing/landing_futor_add.html'
    form_class = LandingAddForm
    success_url = reverse_lazy('admin2:landing_futor_list')


class LandingFutorDelete(LoginRequiredMixin, DeleteView):
    model = LandingFutor
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:landing_futor_list')
