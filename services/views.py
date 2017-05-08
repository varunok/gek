# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from common.mixins import ServiceSiteMixin
from services.helpers import return_list_services
from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, \
    UniversalService


class ServicesSiteView(TemplateView):
    template_name = 'services/services.html'


    def get_context_data(self, **kwargs):
        context = super(ServicesSiteView, self).get_context_data(**kwargs)
        active_service = return_list_services()
        context['services'] = ''
        for service in active_service:
            if active_service.index(service) % 2:
                context['services'] += render_to_string('services/include/services_page_left.html',
                                                        {'service': service})
            else:
                context['services'] += render_to_string('services/include/services_page_right.html',
                                                        {'service': service})
        return context


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
