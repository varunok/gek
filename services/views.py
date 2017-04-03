from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView

from services.models import ServicesRieltor


class ServicesSiteView(TemplateView):
    template_name = 'services/services.html'


class RieltorServiceView(DetailView):
    template_name = 'services/rieltor_service.html'
    context_object_name = 'service_rieltor'

    def get(self, request, *args, **kwargs):
        if not ServicesRieltor.objects.get().is_enable:
            return HttpResponseRedirect('/')
        return super(RieltorServiceView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RieltorServiceView, self).get_context_data(**kwargs)
        context['faqs'] = ServicesRieltor.objects.get().fag.all().order_by('id')
        return context

    def get_object(self, queryset=None):
        return ServicesRieltor.objects.get()
