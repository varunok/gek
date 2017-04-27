# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.views.generic.base import ContextMixin

from admin2.forms import FeedSet, FeedVideoSet
from admin2.models import TrustPageModel
from common.mixins import FormSetMixin


class TrustMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(TrustMixin, self).get_context_data(**kwargs)
        context['content_type'] = ContentType.objects.get_for_model(TrustPageModel).id
        # try:
        context['faqs'] = self.get_object().fag.all().order_by('id')
        return context

    def get_object(self, queryset=None):
        return TrustPageModel.get_solo()


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


class TrustFeed(TrustMixin, FormSetMixin):
    model = TrustPageModel
    template_name = 'admin2/trust/trust_feed.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:trust_feed')
    formset = FeedSet


class TrustFeedVideo(TrustMixin, FormSetMixin):
    model = TrustPageModel
    template_name = 'admin2/trust/trust_feed_video.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:trust_feed_video')
    formset = FeedVideoSet

