# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView
from django.forms import models as model_forms

from admin2.models import IndexPageModel, NewBuildingPageModel, DailyPageModel, BuildingPageModel, OfisPageModel, \
    TrustPageModel, ContactPageModel

class PageList(object):
    LIST_PAGE = [
        IndexPageModel.get_solo(),
        NewBuildingPageModel.get_solo(),
        DailyPageModel.get_solo(),
        BuildingPageModel.get_solo(),
        OfisPageModel.get_solo(),
        TrustPageModel.get_solo(),
        ContactPageModel.get_solo()
    ]


class StaticPageView(LoginRequiredMixin, TemplateView):
    # model = StaticPageModel
    template_name = 'admin2/static_pages/static_pages.html'


    def get_context_data(self, **kwargs):
        context = super(StaticPageView, self).get_context_data(**kwargs)
        context['pages'] = PageList.LIST_PAGE
        return context


class StaticPageDetailView(LoginRequiredMixin, UpdateView):
    template_name = 'admin2/static_pages/static_page_edit.html'
    context_object_name = 'page'
    slug_field = 'slug'
    fields = '__all__'
    success_url = reverse_lazy('admin2:static_pages')

    def get_object(self, *args, **kwargs):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        for page in PageList.LIST_PAGE:
            if page.slug == slug:
                return page
        return None

    def get_form_class(self):
        model = self.object.__class__
        return model_forms.modelform_factory(model, fields=self.fields, exclude=('is_enable',))


def status_page(request):
    if request.POST:
        on = request.POST.get('check')
        page_name = request.POST.get('page_id')
        for page in PageList.LIST_PAGE:
            if page.name == page_name:
                if on:
                    page.is_enable = True
                    page.save()
                    return HttpResponse('Включено')
                else:
                    page.is_enable = False
                    page.save()
                    return HttpResponse('Выключено')
    return HttpResponse(status=500)
