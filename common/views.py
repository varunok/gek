# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, DeleteView

from admin2.form import VideoRieltorServiceSet
from common.mixins import DeleteAjaxMixin
from common.models import Video, FAQ


class MainView(TemplateView):
    template_name = 'index.html'


def save_video(request):
    if request.method == 'POST':
        content_type_id = request.POST.get('content_type', None)
        uuid = request.POST.get('uuid', None)
        model = ContentType.objects.get_for_id(content_type_id)
        model = model.get_object_for_this_type(uuid=uuid)
        form = VideoRieltorServiceSet(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, content='Сохранено')
    return HttpResponse(status=500)


def status_video(request):
    if request.method == 'POST':
        on = request.POST.get('check')
        video_id = request.POST.get('video_id')
        video = Video.objects.get(id=video_id)
        if on:
            video.is_enable = True
            video.save()
            return HttpResponse('Включено')
        else:
            video.is_enable = False
            video.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)


def status_faq(request):
    if request.method == 'POST':
        on = request.POST.get('check')
        content_type_id = request.POST.get('content_type')
        model = ContentType.objects.get_for_id(content_type_id).model_class().get_solo()
        if on:
            model.faq_enable = True
            model.save()
            return HttpResponse('Включено')
        else:
            model.faq_enable = False
            model.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)


def delete_image(request):
    content_type_id = request.GET.get('content_type')
    model = ContentType.objects.get_for_id(content_type_id).model_class().get_solo()
    model.image.delete(save=True)
    return HttpResponse('Удалено')

class ModalVideo(View):
    pk = 'pk'
    model = Video
    template_name = 'common/video_modal.html'
    context_name = 'video'

    def get_object(self, **kwargs):
        return self.model.objects.get(id=self.kwargs.get(self.pk))

    def get_context(self):
        if self.context_name:
            self.object = self.get_object()
            return {self.context_name: self.object}

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        content = render_to_string(self.template_name, context)
        return HttpResponse(content)


def create_faq(request):
    content_type_id = request.GET.get('content_type')
    model_id = request.GET.get('model_id')
    model = ContentType.objects.get_for_id(content_type_id)
    faq = FAQ.objects.create(content_type=model,
                             object_id=model_id)
    context = render_to_string('common/faq_item.html', {'faq': faq})
    return HttpResponse(context)


def save_faq(request):
    if request.method == 'POST':
        for key in request.POST:
            if 'faq-answer' in key:
                faq_id = key.split('-')[-1]
                faq_ask = 'faq-ask-' + faq_id
                faq_answer = request.POST.get(key)
                faq_ask = request.POST.get(faq_ask)
                FAQ.objects.filter(id=faq_id).update(title=faq_ask, text=faq_answer)
        return HttpResponse()
    return HttpResponse(status=500)


class FAQDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = FAQ
    pk_url_kwarg = 'id'

