# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from admin2.forms import RieltorServiceForm, VideoRieltorServiceSet, ValuationForm, VideoServiceSet
from services.models import ServicesRieltor, Valuation


class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = 'admin2/services/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['rieltor_service_content_type'] = ContentType.objects.get_for_model(ServicesRieltor).id
        context['rieltor_service'] = ServicesRieltor.objects.get()
        context['valuation'] = Valuation.get_solo()
        context['valuation_content_type'] = ContentType.objects.get_for_model(Valuation).id
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


class ValuationServiceView(UpdateView):
    model = Valuation
    form_class = ValuationForm
    template_name = 'admin2/services/valuation_edit.html'
    context_object_name = 'valuation'
    success_url = reverse_lazy('admin2:services')

    def get_object(self, queryset=None):
        return Valuation.objects.get()

    def get_context_data(self, **kwargs):
        context = super(ValuationServiceView, self).get_context_data(**kwargs)
        context['video_form'] = VideoServiceSet(instance=Valuation.objects.get())
        context['video_check'] = Valuation.get_solo().videos.all().order_by('id')
        context['faqs'] = Valuation.get_solo().fag.all().order_by('id')
        context['content_type'] = ContentType.objects.get_for_model(Valuation).id
        return context







def status_service(request):
    if request.method == 'POST':
        on = request.POST.get('check')
        content_type_id = request.POST.get('content_type')
        service = ContentType.objects.get_for_id(content_type_id).model_class().get_solo()
        if on:
            service.is_enable = True
            service.save()
            return HttpResponse('Включено')
        else:
            service.is_enable = False
            service.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)
