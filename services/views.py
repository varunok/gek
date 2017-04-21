from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView

from common.mixins import ServiceSiteMixin
from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, \
    UniversalService


class ServicesSiteView(TemplateView):
    template_name = 'services/services.html'


class RieltorServiceView(ServiceSiteMixin):
    template_name = 'services/rieltor_service.html'
    context_object_name = 'service_rieltor'
    model = ServicesRieltor


class ValuationView(ServiceSiteMixin):
    template_name = 'services/valuation.html'
    context_object_name = 'valuation'
    model = Valuation


class RepairView(ServiceSiteMixin):
    template_name = 'services/repair.html'
    context_object_name = 'repair'
    model = Repair


class InsuranceView(ServiceSiteMixin):
    template_name = 'services/insurance.html'
    context_object_name = 'insurance'
    model = Insurance


class CleaningView(ServiceSiteMixin):
    template_name = 'services/cleaning.html'
    context_object_name = 'cleaning'
    model = Cleaning


class InstallationWaterView(ServiceSiteMixin):
    template_name = 'services/installation_water.html'
    context_object_name = 'installation_water'
    model = InstallationWater


class UniversalView(ServiceSiteMixin):
    template_name = 'services/universal.html'
    context_object_name = 'universal'
    model = UniversalService