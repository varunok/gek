# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from users.views import AdminsView, AdminDetail, ChangePass, AdminCreate, AdminDeleteView

urlpatterns = [
    url('^admins/$', AdminsView.as_view(), name='admins'),
    url('^admins/delete/(?P<id>[\d-]+)/$', AdminDeleteView.as_view(), name='admins'),
    url('^profile/(?P<id>[\d-]+)/$', AdminDetail.as_view(), name='profile'),
    url('^profile/create/$', AdminCreate.as_view(), name='admin_create'),
    url('change-pass/$', ChangePass.as_view(), name='chnge_pass'),
]

