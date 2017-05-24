# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dal_select2.views import Select2QuerySetView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.db.models import F
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic.detail import SingleObjectMixin, BaseDetailView, DetailView
from django.views.generic.list import BaseListView, MultipleObjectMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import UpdateView

from common.models import BasePacket, MidlePacket, ExpertPacket



class MessageMixin(SuccessMessageMixin):
    success_message = "Сохранено"


class SuccesMixin():
    object = None
    def get_success_url(self):
        return self.object.get_edit_url()


class DeleteAjaxMixin(SingleObjectMixin):

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)


class ViewsCountMixin(BaseDetailView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views = F('views') + 1
        self.object.save()
        return super(ViewsCountMixin, self).get(request, *args, **kwargs)


class DinamicNextMixin(BaseListView):
    dinamic_template_name = None
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(DinamicNextMixin, self).get_context_data(**kwargs)
        context['count_next'] = self.get_count_next()
        return context

    def get_count_next(self):
        count_next = self.get_queryset().count() - self.paginate_by
        count_next = 0 if count_next <= 0 else count_next
        return count_next

    def get(self, request, *args, **kwargs):
        page = self.request.GET.get('page')
        section = self.request.GET.get('section')
        if page:
            object_list = self.get_queryset()
            if section:
                object_list = object_list.filter(sections=section)
            paginator = self.get_paginator(object_list, self.paginate_by)
            data = JsonResponse({
                'next': paginator.page(page).has_next(),
                'html': render_to_string(self.dinamic_template_name,
                                             {self.context_object_name: paginator.page(page).object_list}),
                'obj': len(paginator.page(page).object_list)
            })
            return HttpResponse(data)
        return super(DinamicNextMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        page = self.request.POST.get('page')
        if page:
            object_list = self.get_queryset()
            paginator = self.get_paginator(object_list, self.paginate_by)
            data = JsonResponse({
                'next': paginator.page(page).has_next(),
                'html': render_to_string(self.dinamic_template_name,
                                         {self.context_object_name: paginator.page(page).object_list,
                                          'count_next': self.get_count_next()}),
                'obj': len(paginator.page(page).object_list)
            })
            return HttpResponse(data)
        # return super(DinamicNextMixin, self).post(request, *args, **kwargs)



class ServiceSiteMixin(DetailView):

    def get(self, request, *args, **kwargs):
        if not self.get_object().is_enable:
            return HttpResponseRedirect('/')
        return super(ServiceSiteMixin, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ServiceSiteMixin, self).get_context_data(**kwargs)
        try:
            context['faqs'] = self.get_object().fag.all().order_by('id')
        except AttributeError:
            pass
        try:
            context['images'] = self.get_object().images.all().order_by('id')
        except AttributeError:
            pass
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            return self.model.objects.get(slug=slug)
        return self.model.objects.get()


class ServicesMixin(SuccesMixin, MessageMixin, UpdateView):
    video_form = None
    advantage_form = None

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        if pk:
            return self.model.objects.get(pk=pk)
        return self.model.objects.get()

    def get_context_data(self, **kwargs):
        context = super(ServicesMixin, self).get_context_data(**kwargs)
        context['video_form'] = self.video_form(instance=self.get_object())
        try:
            context['advantage_form'] = self.advantage_form(instance=self.get_object())
        except TypeError:
            pass
        context['video_check'] = self.get_object().videos.all().order_by('id')
        try:
            context['faqs'] = self.get_object().fag.all().order_by('id')
        except AttributeError:
            pass
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        try:
            context['base_content_type'] = ContentType.objects.get_for_model(BasePacket).id
            context['midle_content_type'] = ContentType.objects.get_for_model(MidlePacket).id
            context['expert_content_type'] = ContentType.objects.get_for_model(ExpertPacket).id
        except AttributeError:
            pass
        return context


class Select2QuerySetViewCustom(Select2QuerySetView):
    def get_create_option(self, context, q):
        """Form the correct create_option to append to results."""
        create_option = []
        display_create_option = False
        if self.create_field and q:
            page_obj = context.get('page_obj', None)
            if page_obj is None or page_obj.number == 1:
                display_create_option = True

        if display_create_option and self.has_add_permission(self.request):
            create_option = [{
                'id': q,
                'text': _('Создать "%(new_value)s"') % {'new_value': q},
                'create_id': True,
            }]
        return create_option

    def get_queryset(self):
        qs = MultipleObjectMixin.get_queryset(self)
        if self.q:
            create_field = '{0}__icontains'.format(self.create_field)
            qs = qs.filter(**{create_field: self.q})
            print(qs)

        return qs


class FormSetMixin(UpdateView):
    formset = None

    def get(self, request, *args, **kwargs):
        self.object = None
        if not self.formset:
            self.formset = self.get_formset(request)
        formset = self.formset(instance=self.get_object())
        return self.render_to_response(
            self.get_context_data(
                                  formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        if not self.formset:
            self.formset = self.get_formset(request)
        formset =  self.formset(self.request.POST, self.request.FILES, instance=self.get_object())
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def form_valid(self, formset):
        self.object = formset.save()
        if not self.success_url:
            self.success_url = self.get_success_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, formset):
        return self.render_to_response(
            self.get_context_data(formset=formset))



