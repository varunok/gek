# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from admin2.models import Settings


class SettingsView(UpdateView):
    model = Settings
    template_name = 'admin2/settings/settings.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:settings')

    def get_object(self, queryset=None):
        return Settings.objects.get()

    # def get_slug_field(self):
