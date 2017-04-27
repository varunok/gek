# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from admin2.models import ContactPageModel


class Contacts(DetailView):
    # model = TrustPageModel
    template_name = 'contact/contacts.html'

    def get_object(self, queryset=None):
        return ContactPageModel.get_solo()