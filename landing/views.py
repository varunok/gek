# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.redirects.models import Redirect
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import resolve
from django.views.generic import TemplateView, DetailView

from landing.helpers import query_landing
from landing.models import Landing


# class LandingPage(DetailView):
#     model = Landing
#     template_name = 'landing/multilending.html'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super(LandingPage, self).get_context_data(**kwargs)
#         context['object_list'] = query_landing(self.object)
#         return context


def redirect_view(request, slug):
    try:
        object = Landing.objects.get(slug=slug)
        object_list = query_landing(object)
        context = {
            'object': object,
            'object_list': object_list
        }
        return render(request, 'landing/multilending.html', context)
    except ObjectDoesNotExist:
        current_site = get_current_site(request)
        full_path = request.get_full_path()
        r = get_object_or_404(Redirect, site=current_site, new_path__icontains=full_path)
        view, args, kwargs = resolve(r.old_path)
        kwargs['request'] = request
        return view(*args, **kwargs)

