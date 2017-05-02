# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.banners_views import Banners, EditBannerImage, SideBanner, EditBannerCode
from banners.models import DownBanner

urlpatterns = [
    # POLLS
    url(r'^banners/$',Banners.as_view(),name='banners'),
    url(r'^banners/downbanners-image/$',EditBannerImage.as_view(model=DownBanner),name='downbanners_image'),
    url(r'^banners/sidebanners-image/$',EditBannerImage.as_view(model=SideBanner),name='sidebanners_image'),
    url(r'^banners/downbanners-code/$',EditBannerCode.as_view(model=DownBanner),name='downbanners_code'),
    url(r'^banners/sidebanners-code/$',EditBannerCode.as_view(model=SideBanner),name='sidebanners_code'),
]