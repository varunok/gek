# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = 'admin2/services/services.html'