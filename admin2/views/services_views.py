# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from admin2.forms import RieltorServiceForm, VideoRieltorServiceSet, ValuationForm, VideoServiceSet, RepairForm, \
    InsuranceForm
from services.models import ServicesRieltor, Valuation, Repair, Insurance


class ServicesMixin(UpdateView):
    video_form = None

    def get_object(self, queryset=None):
        return self.model.objects.get()

    def get_context_data(self, **kwargs):
        context = super(ServicesMixin, self).get_context_data(**kwargs)
        context['video_form'] = self.video_form(instance=self.model.objects.get())
        context['video_check'] = self.model.get_solo().videos.all().order_by('id')
        try:
            context['faqs'] = self.model.get_solo().fag.all().order_by('id')
        except AttributeError:
            pass
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        return context



class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = 'admin2/services/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['rieltor_service_content_type'] = ContentType.objects.get_for_model(ServicesRieltor).id
        context['rieltor_service'] = ServicesRieltor.get_solo()
        context['valuation'] = Valuation.get_solo()
        context['valuation_content_type'] = ContentType.objects.get_for_model(Valuation).id
        context['repair'] = Repair.get_solo()
        context['repair_content_type'] = ContentType.objects.get_for_model(Repair).id
        context['insurence'] = Insurance.get_solo()
        context['insurence_content_type'] = ContentType.objects.get_for_model(Insurance).id
        return context


class RieltorServiceView(ServicesMixin):
    model = ServicesRieltor
    form_class = RieltorServiceForm
    template_name = 'admin2/services/rieltor_service_edit.html'
    context_object_name = 'rieltor_service'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoRieltorServiceSet


class ValuationServiceView(ServicesMixin):
    model = Valuation
    form_class = ValuationForm
    template_name = 'admin2/services/valuation_edit.html'
    context_object_name = 'valuation'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet


class RepairServiceView(ServicesMixin):
    model = Repair
    form_class = RepairForm
    template_name = 'admin2/services/repair_edit.html'
    context_object_name = 'repair'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet

    def get_context_data(self, **kwargs):
        context = super(RepairServiceView, self).get_context_data(**kwargs)
        context['repairs_table'] = self.model.objects.get().repairs.all().order_by('id')
        return context


class InsurenceServiceView(ServicesMixin):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'admin2/services/insurence_edit.html'
    context_object_name = 'insurance'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet


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
