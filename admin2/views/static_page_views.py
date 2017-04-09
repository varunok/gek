# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView

from admin2.models import IndexPageModel, NewBuildingPageModel, DailyPageModel


LIST_PAGE = [IndexPageModel.get_solo(), NewBuildingPageModel.get_solo(), DailyPageModel.get_solo()]


class StaticPageView(LoginRequiredMixin, TemplateView):
    # model = StaticPageModel
    template_name = 'admin2/static_pages/static_pages.html'
    # context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super(StaticPageView, self).get_context_data(**kwargs)
        context['pages'] = LIST_PAGE
        return context


class StaticPageDetailView(LoginRequiredMixin, UpdateView):
    template_name = 'admin2/static_pages/static_page_edit.html'
    context_object_name = 'page'
    slug_field = 'name'
    fields = '__all__'
    exclude = 'is_enable',
    success_url = reverse_lazy('admin2:static_pages')

    def get_object(self, *args, **kwargs):
        print(self.kwargs)
        print(self.args)
        pk = self.kwargs.get('pk')
        for page in LIST_PAGE:
            if page.name == pk:
                return page
        return None


def status_page(request):
    if request.POST:
        on = request.POST.get('check')
        page_id = request.POST.get('page_id')
        page = IndexPageModel.objects.get(id=page_id)
        if on:
            page.is_enable = True
            page.save()
            return HttpResponse('Включено')
        else:
            page.is_enable = False
            page.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)
