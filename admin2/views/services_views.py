# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from admin2.form import RieltorServiceForm, VideoRieltorServiceSet
from services.models import ServicesRieltor


class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = 'admin2/services/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['rieltor_service'] = ServicesRieltor.objects.get()
        return context


class RieltorServiceView(UpdateView):
    model = ServicesRieltor
    form_class = RieltorServiceForm
    template_name = 'admin2/services/rieltor_service_edit.html'
    context_object_name = 'rieltor_service'
    success_url = reverse_lazy('admin2:services')

    def get_object(self, queryset=None):
        return ServicesRieltor.objects.get()

    def get_context_data(self, **kwargs):
        context = super(RieltorServiceView, self).get_context_data(**kwargs)
        context['video_form'] = VideoRieltorServiceSet(instance=ServicesRieltor.objects.get())
        context['video_check'] = ServicesRieltor.get_solo().videos.all().order_by('id')
        context['faqs'] = ServicesRieltor.get_solo().fag.all().order_by('id')
        context['content_type'] = ContentType.objects.get_for_model(ServicesRieltor).id
        return context


def status_service(request):
    if request.method == 'POST':
        on = request.POST.get('check')
        page_id = request.POST.get('page_id')
        service = ServicesRieltor.objects.get()
        if on:
            service.is_enable = True
            service.save()
            return HttpResponse('Включено')
        else:
            service.is_enable = False
            service.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)
