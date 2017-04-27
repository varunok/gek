# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from admin2.models import TrustPageModel


class Trust(DetailView):
    # model = TrustPageModel
    template_name = 'trust/trust.html'

    def get_object(self, queryset=None):
        return TrustPageModel.get_solo()