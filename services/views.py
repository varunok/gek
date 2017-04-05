from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView

from services.models import ServicesRieltor, Valuation, Repair


class ServicesSiteView(TemplateView):
    template_name = 'services/services.html'


class ServiceSiteMixin(DetailView):

    def get(self, request, *args, **kwargs):
        if not self.model.objects.get().is_enable:
            return HttpResponseRedirect('/')
        return super(ServiceSiteMixin, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ServiceSiteMixin, self).get_context_data(**kwargs)
        try:
            context['faqs'] = self.model.objects.get().fag.all().order_by('id')
        except AttributeError:
            pass
        return context

    def get_object(self, queryset=None):
        return self.model.objects.get()


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
