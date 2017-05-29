# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView

from admin2.forms import RieltorServiceForm, VideoRieltorServiceSet, ValuationForm, VideoServiceSet, RepairForm, \
    InsuranceForm, CleaningForm, InstallationWaterForm, UniversalServiceForm, UniversalServiceCreateForm, AdvantageSet, \
    PartnerForm
from admin2.mixins import AccesMixin
from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, \
    UniversalService, Partner

from common.mixins import DeleteAjaxMixin, ServicesMixin, SuccesMixin, MessageMixin


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
        context['cleaning'] = Cleaning.get_solo()
        context['cleaning_content_type'] = ContentType.objects.get_for_model(Cleaning).id
        context['installation_water'] = InstallationWater.get_solo()
        context['installation_water_content_type'] = ContentType.objects.get_for_model(InstallationWater).id
        context['universals'] = UniversalService.objects.all()
        context['universal_content_type'] = ContentType.objects.get_for_model(UniversalService).id
        return context


class RieltorServiceView(ServicesMixin):
    model = ServicesRieltor
    form_class = RieltorServiceForm
    template_name = 'admin2/services/rieltor_service_edit.html'
    context_object_name = 'rieltor_service'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoRieltorServiceSet
    partner_form = PartnerForm


class ValuationServiceView(ServicesMixin):
    model = Valuation
    form_class = ValuationForm
    template_name = 'admin2/services/valuation_edit.html'
    context_object_name = 'valuation'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet
    partner_form = PartnerForm


class RepairServiceView(ServicesMixin):
    model = Repair
    form_class = RepairForm
    template_name = 'admin2/services/repair_edit.html'
    context_object_name = 'repair'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet
    partner_form = PartnerForm

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
    partner_form = PartnerForm


class CleaningServiceView(ServicesMixin):
    model = Cleaning
    form_class = CleaningForm
    template_name = 'admin2/services/cleaning_edit.html'
    context_object_name = 'cleaning'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet
    partner_form = PartnerForm


class InstallationWaterServiceView(ServicesMixin):
    model = InstallationWater
    form_class = InstallationWaterForm
    template_name = 'admin2/services/installation_water_edit.html'
    context_object_name = 'installation_water'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet
    partner_form = PartnerForm


class UniversalServiceView(ServicesMixin):
    model = UniversalService
    form_class = UniversalServiceForm
    template_name = 'admin2/services/universal_edit.html'
    context_object_name = 'universal'
    success_url = reverse_lazy('admin2:services')
    video_form = VideoServiceSet
    advantage_form = AdvantageSet
    partner_form = PartnerForm


class UniversalServiceCreate(LoginRequiredMixin, SuccesMixin, MessageMixin, CreateView):
    model = UniversalService
    form_class = UniversalServiceCreateForm
    template_name = 'admin2/services/universal_edit.html'

    def get_success_url(self):
        return reverse_lazy('admin2:universal_edit', args=[self.object.id])


class UniversalServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = UniversalService
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:services')


def status_service(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            on = request.POST.get('check')
            id = request.POST.get('id')
            content_type_id = request.POST.get('content_type')
            if id:
                service = ContentType.objects.get_for_id(content_type_id).model_class().objects.get(id=id)
            else:
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


def partner_create(request):
    if request.method == 'POST':
        partner = None
        partner_id = request.POST.get('partner_id')
        if partner_id:
            partner = Partner.objects.get(id=partner_id)
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
    return HttpResponse(status=500)


def partner_edit(request, object_id):
    partner = get_object_or_404(Partner, id=object_id)
    partner_form = PartnerForm(instance=partner)
    context = {
        'partner_form': partner_form,
        'content_type': partner.content_type_id,
        'object': {'id':partner.object_id},
        'partner': partner.id
    }
    return render(request, 'admin2/services/include/item/partner_form.html', context)


def get_partner_list(request, content_type, object_id):
    service = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
    partners = service.partners.all()
    return render(request, 'admin2/services/include/item/partners.html', {'partners': partners})


class DellPartner(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Partner
