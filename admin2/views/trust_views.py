# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, DetailView, FormView
from django.views.generic.base import ContextMixin, View

from admin2.forms import FeedSet, FeedVideoSet
from admin2.models import TrustPageModel
from common.models import Feed


class TrustMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(TrustMixin, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(TrustPageModel).id
        # try:
        context['faqs'] = self.get_object().fag.all().order_by('id')
        return context

    def get_object(self, queryset=None):
        return TrustPageModel.get_solo()


class FeedMixin(UpdateView):
    formset = None

    def get(self, request, *args, **kwargs):
        self.object = None
        formset = self.formset(instance=TrustPageModel.get_solo())
        return self.render_to_response(
            self.get_context_data(
                                  formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        formset =  self.formset(self.request.POST,self.request.FILES, instance=TrustPageModel.get_solo())
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def form_valid(self, formset):
        self.object = formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, formset):
        return self.render_to_response(
            self.get_context_data(formset=formset))



class TrustDetail(TrustMixin, UpdateView):
    template_name = 'admin2/trust/trust.html'
    context_object_name = 'trust'
    slug_field = 'slug'
    fields = '__all__'
    success_url = reverse_lazy('admin2:trust')


class TrustGallery(TrustMixin, DetailView):
    template_name = 'admin2/trust/trust_gallery.html'


class TrustFaq(TrustMixin, DetailView):
    template_name = 'admin2/trust/trust_faq.html'


class TrustFeed(TrustMixin, FeedMixin):
    model = TrustPageModel
    template_name = 'admin2/trust/trust_feed.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:trust_feed')
    formset = FeedSet


class TrustFeedVideo(TrustMixin, FeedMixin):
    model = TrustPageModel
    template_name = 'admin2/trust/trust_feed_video.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:trust_feed_video')
    formset = FeedVideoSet

