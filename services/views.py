from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView

from services.models import ServicesRieltor


class ServicesSiteView(TemplateView):
    template_name = 'services/services.html'


class RieltorServiceView(TemplateView):
    template_name = 'services/rieltor_service.html'

    def get_context_data(self, **kwargs):
        context = super(RieltorServiceView, self).get_context_data(**kwargs)
        context['faqs'] = ServicesRieltor.objects.get().fag.all().order_by('id')
        return context
