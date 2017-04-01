# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
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
        if self.request.POST and 'save_video' in self.request.POST:
            context['video_form'] = VideoRieltorServiceSet(self.request.POST,
                                                           instance=ServicesRieltor.objects.get())
        else:
            context['video_form'] = VideoRieltorServiceSet(instance=ServicesRieltor.objects.get())
        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if 'save_video' in self.request.POST:
            # self.object =None
            form = self.get_form(form_class=VideoRieltorServiceSet)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     if 'save_video' in self.request.POST:
    #         ctx = self.get_context_data()
    #         video_form = ctx.get('video_form')
    #         if video_form.is_valid():
    #             video_form.save()
    #             return redirect(self.get_success_url())
    #         else:
    #             return self.render_to_response(self.get_context_data(form=video_form))
    #     else:
    #         return super(RieltorServiceView, self).form_valid(form)


def status_service(request):
    if request.POST:
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
