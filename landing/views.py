# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.redirects.models import Redirect
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import resolve, Resolver404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView

from landing.helpers import query_landing, get_seo
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
from landingpage.models import SuperlandingSettings
from landingpage.views import Superlending


def redirect_view(request, slug):
    if False:
        pass
    # if SuperlandingSettings.get_solo().enabled:
    #     return Superlending
    else:
        try:
            object = Landing.objects.get(slug=slug)
            object_list = query_landing(object)

            paginator = Paginator(object_list, 30)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)

            context = {
                'object': object,
                'object_list': object_list,
                'seo': get_seo(request) or object
            }
            return render(request, 'landing/multilending.html', context)
        except ObjectDoesNotExist:
            current_site = get_current_site(request)
            full_path = request.get_full_path()
            r = get_object_or_404(Redirect, site=current_site,
                                  new_path__icontains=full_path)
            view, args, kwargs = resolve(r.old_path)
            if not view.__dict__:
                raise Resolver404()
            kwargs['request'] = request
            return view(*args, **kwargs)

