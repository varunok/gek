# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DeleteView, DetailView

from admin2.forms import VideoRieltorServiceSet, AdvantageSet
from admin2.models import IndexPageModel, ActiveFranchise
from common.forms import SaveApplicationForm
from common.helpers import sending_email
from common.mixins import DeleteAjaxMixin
from common.models import Video, FAQ, TableRepair, Photo, TextPacket
from rieltor_object.models import Infrastructure, Accommodations, ApartmentNext, NewBuilding, Building, \
    Ofice
from seo.mixins import SEOMixin


class MainView(SEOMixin, DetailView):
    template_name = 'index.html'
    seo_model = IndexPageModel

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['offices'] = Ofice.objects.vips().order_by('?')
        context['buildings'] = Building.objects.vips().order_by('?')
        context['newbuildings'] = NewBuilding.objects.order_by('?')
        context['indexpagemodel'] = IndexPageModel.get_solo()
        return context

    def get_object(self, queryset=None):
        return IndexPageModel.get_solo()


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


def save_advantage(request):
    if request.method == 'POST':
        content_type_id = request.POST.get('content_type', None)
        uuid = request.POST.get('uuid', None)
        model = ContentType.objects.get_for_id(content_type_id)
        model = model.get_object_for_this_type(uuid=uuid)
        form = AdvantageSet(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, content='Сохранено')
        if form.errors:
            return HttpResponse(status=500, content='Не заполнени все поля')
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


def status_common(request):
    if request.method == 'POST':
        on = request.POST.get('check')
        type_eneble = request.POST.get('type')
        model_id = request.POST.get('model_id')
        content_type_id = request.POST.get('content_type')
        model = ContentType.objects.get_for_id(content_type_id).model_class().objects.get(id=model_id)
        if on:
            if type_eneble == 'faqs':
                model.faq_enable = True
                model.repairs_enable = True
            elif type_eneble == 'packet':
                model.packet_enable = True
            model.save()
            return HttpResponse('Включено')
        else:
            if type_eneble == 'faqs':
                model.faq_enable = False
                model.repairs_enable = False
            elif type_eneble == 'packet':
                model.packet_enable = False
            model.save()
            return HttpResponse('Выключено')
    return HttpResponse(status=500)


def delete_image(request):
    content_type_id = request.GET.get('content_type')
    id = request.GET.get('id')
    title_image = request.GET.get('title_image')
    seo_image = request.GET.get('seo_image')
    form_image = request.GET.get('form_image')
    if id:
        model = ContentType.objects.get_for_id(content_type_id).model_class().objects.get(id=id)
    else:
        model = ContentType.objects.get_for_id(content_type_id).model_class().get_solo()
    if title_image:
        try:
            model.title_image.delete(save=True)
        except AttributeError:
            if hasattr(model, 'image_avatar'):
                model.image_avatar.delete(save=True)
                return HttpResponse('Удалено')
            model.image_seo.delete(save=True)
        return HttpResponse('Удалено')
    if seo_image:
        model.image_seo.delete(save=True)
        return HttpResponse('Удалено')
    if form_image:
        model.image_form.delete(save=True)
        return HttpResponse('Удалено')
    else:
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


def create_rep(request):
    content_type_id = request.GET.get('content_type')
    model_id = request.GET.get('model_id')
    model = ContentType.objects.get_for_id(content_type_id)
    rep = TableRepair.objects.create(content_type=model,
                                     object_id=model_id)
    context = render_to_string('common/rep_item.html', {'rep': rep})
    return HttpResponse(context)


def save_rep(request):
    if request.method == 'POST':
        for key in request.POST:
            if 'rep-name' in key:
                rep_id = key.split('-')[-1]
                rep_price = 'rep-price-' + rep_id
                rep_name = request.POST.get(key)
                rep_price = request.POST.get(rep_price)
                TableRepair.objects.filter(id=rep_id).update(name=rep_name, price=rep_price)
        return HttpResponse()
    return HttpResponse(status=500)


class RepairDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = TableRepair
    pk_url_kwarg = 'id'


class DeletePhotoView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Photo
    pk_url_kwarg = 'id'


class SavePhotoView(View):
    model = Photo
    template_name = 'common/photo_items.html'

    def post(self, request, *args, **kwargs):
        list_callback = []
        content_type = self.get_content_type()
        for image in self.request.FILES.getlist('image'):
            photo = Photo.objects.create(image=image,
                                         content_type=content_type,
                                         object_id=self.get_obj_id())
            list_callback.append(photo)
        response = render_to_string(self.template_name, {'images': list_callback})
        return HttpResponse(response)

    def get_content_type(self):
        content_type_id = self.request.POST.get('content_type')
        return ContentType.objects.get_for_id(content_type_id)

    def get_obj_id(self):
        return self.request.POST.get('object_id')


def packet_text_save(request):
    if request.method == 'POST':
        packet_content_type = request.POST.get('packet_content_type')
        packet_id = request.POST.get('packet_id')
        content_type = ContentType.objects.get_for_id(packet_content_type)
        # packet = packet_model.objects.get(id=packet_id)
        # print(packet)
        for item in request.POST:
            if 'item' in item:
                item = request.POST.get(item)
                TextPacket.objects.create(
                    text=item,
                    content_type=content_type,
                    object_id=packet_id)
        return HttpResponse(status=200)
    return HttpResponse(status=500)


def packet_create(request):
    if request.method == 'POST':
        packet_content_type = request.POST.get('packet_content_type')
        service_content_type = request.POST.get('service_content_type')
        model_id = request.POST.get('model_id')
        packet = ContentType.objects.get_for_id(packet_content_type).model_class()
        service_model = ContentType.objects.get_for_id(service_content_type).model_class().objects.get(id=model_id)
        packet = packet.objects.create()
        packet_name = packet.__name_packet__
        setattr(service_model, packet_name, packet)
        service_model.save()
        return render(request, 'common/packet_item.html', {'packet': packet,
                                                           'packet_content_type': packet_content_type,
                                                           'color': get_color(packet)})
    return HttpResponse(status=500)


def get_color(packet):
    if packet.__name_packet__ == 'base_packet':
        return '#03baf7'
    if packet.__name_packet__ == 'midle_packet':
        return '#20ce5d'
    if packet.__name_packet__ == 'expert_packet':
        return '#f8bd2f'


def save_infrastructure(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        content_type = request.POST.get('content_type')
        image = request.FILES.get('image')
        title = request.POST.get('title')
        add = request.POST.get('add')
        data = {}
        if not title or not image:
            return HttpResponse(status=500, content='Заголовок і картинка обязательни')
        infra = Infrastructure.objects.create(
            title=title,
            image=image
        )
        data['item'] = render_to_string('common/infra_left.html', {'infrastructure':infra, 'content_type':content_type})
        data['add'] = False
        if add:
            obj = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
            obj.infrastructures.add(infra)
            data['add'] = True
            data['item'] = render_to_string('common/infra_right.html', {'infrastructure': infra, 'content_type':content_type})
        data = JsonResponse(data)
        return HttpResponse(data)
    return HttpResponse(status=500)


def related_infrastructure(request, content_type, infra_id, object_id):
    obj = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
    infra = Infrastructure.objects.get(id=infra_id)
    if infra in obj.infrastructures.all():
        obj.infrastructures.remove(infra)
        return HttpResponse('Удалено')
    obj.infrastructures.add(infra)
    return HttpResponse('Добавлено')


def save_accommodations(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        content_type = request.POST.get('content_type')
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        add = request.POST.get('add')
        data = {}
        if not title or not image:
            return HttpResponse(status=500, content='Заголовок і картинка обязательни')
        acom = Accommodations.objects.create(
            title=title,
            description=description,
            image=image
        )
        data['item'] = render_to_string('common/acom_left.html', {'accommodation':acom, 'content_type':content_type})
        data['add'] = False
        if add:
            obj = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
            obj.accommodations.add(acom)
            data['add'] = True
            data['item'] = render_to_string('common/acom_right.html', {'accommodation': acom, 'content_type':content_type})
        data = JsonResponse(data)
        return HttpResponse(data)
    return HttpResponse(status=500)


def related_accommodations(request, content_type, acom_id, object_id):
    obj = ContentType.objects.get_for_id(content_type).model_class().objects.get(id=object_id)
    acom = Accommodations.objects.get(id=acom_id)
    if acom in obj.accommodations.all():
        obj.accommodations.remove(acom)
        return HttpResponse('Удалено')
    obj.accommodations.add(acom)
    return HttpResponse('Добавлено')


def save_apartment_next(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        content_type = request.POST.get('content_type')
        name = request.POST.get('name')
        value = request.POST.get('value')
        content_type = ContentType.objects.get_for_id(content_type)
        apartment_next = ApartmentNext.objects.create(
            name=name,
            value=value,
            object_id=object_id,
            content_type = content_type
        )
        item = render_to_string('common/apartment_next_item.html', {'object': apartment_next, 'next':apartment_next})
        data = JsonResponse({
            'item': item
        })
        return HttpResponse(data)
    return HttpResponse(status=500)

def delete_apartment_next(request, id):
    ApartmentNext.objects.get(id=id).delete()
    return HttpResponse()


class SaveApplication(View):
    form_class = SaveApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            sending_email(form.instance)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

