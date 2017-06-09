# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from admin2.forms import ScheduleSet, ContactForm
from admin2.models import ContactPageModel
from common.mixins import FormSetMixin


class ContactUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'admin2/contact/contact.html'
    context_object_name = 'contact'
    slug_field = 'slug'
    form_class = ContactForm
    success_url = reverse_lazy('admin2:contact')

    def get_object(self, queryset=None):
        return ContactPageModel.get_solo()

    def get_context_data(self, **kwargs):
        context = super(ContactUpdate, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(ContactPageModel).id
        return context


class ContactSchedule(LoginRequiredMixin, FormSetMixin, UpdateView):
    model = ContactPageModel
    template_name = 'admin2/contact/contact_shedule.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:contact_schedule')
    formset = ScheduleSet

    def get_object(self, queryset=None):
        return ContactPageModel.get_solo()
