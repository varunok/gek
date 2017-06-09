# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from common.mixins import ViewsCountMixin
from seo.mixins import SEOMixin
from videos.models import Videos


class VideosList(SEOMixin, ListView):
    model = Videos
    template_name = 'videos/video_list.html'

    def get_queryset(self):
        self.object_list = self.model.objects.all()
        if self.request.GET.get('q'):
            self.object_list = self.object_list.filter(description__icontains=self.request.GET.get('q'))
        return self.object_list


class VideosDetail(SEOMixin, ViewsCountMixin, DetailView):
    model = Videos
    template_name = 'videos/video_detail.html'
    pk_url_kwarg = 'pk'
