# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from admin2.models import StaticPageModel


class StaticPageView(ListView):
    model = StaticPageModel
    template_name = 'admin2/static_pages/static_pages.html'
    context_object_name = 'pages'


class StaticPageDetailView(UpdateView):
    model = StaticPageModel
    template_name = 'admin2/static_pages/static_page_detail.html'
    context_object_name = 'page'
    slug_field = 'id'
    fields = '__all__'
    success_url = reverse_lazy('admin2:static_pages')


def status_page(request):
    if request.POST:
        on = request.POST.get('check')
        page_id = request.POST.get('page_id')
        page = StaticPageModel.objects.get(id=page_id)
        if on:
            page.is_enable = True
            page.save()
            return HttpResponse('Включено')
        else:
            page.is_enable = False
            page.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)