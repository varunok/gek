# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import login_views, main_views, articles_views, static_page_views, services_views
from admin2.views import settings_views
from common.views import save_video, status_video, ModalVideo, create_faq, save_faq, FAQDeleteView, \
    delete_image, create_rep, save_rep, RepairDeleteView, status_common, SavePhotoView, DeletePhotoView, \
    packet_text_save, packet_create, save_advantage

urlpatterns = [
    # login views
    url('^login/$', login_views.LoginRememberView.as_view(), name='auth_login'),
    url('^logout/$', login_views.logout_view, name='auth_logout'),

    # COMMON
    url('save-video/$', save_video, name='save_video'),
    url('save-advantage/$', save_advantage, name='save_advantage'),
    url(
        r'status_faq',
        status_common,
        name='status_faq'
    ),
    url(
        r'status_rep',
        status_common,
        name='status_rep'
    ),
    url(
        r'status_packet',
        status_common,
        name='status_packet'
    ),
    url(
        r'packet-text-save',
        packet_text_save,
        name='packet_text_save'
    ),
    url(
        r'packet-create',
        packet_create,
        name='packet_create'
    ),
    url(
        r'delete-image',
        delete_image,
        name='delete_image'
    ),
    url(
        r'status_video',
        status_video,
        name='status_video'
    ),
    url(
        r'modal-video/(?P<pk>[\w-]+)/$',
        ModalVideo.as_view(),
        name='modal_video'
    ),
    url(
        r'create-faq/$',
        create_faq,
        name='create_faq'
    ),
    url(
        r'save-faq/$',
        save_faq,
        name='save_faq'
    ),
    url(
        r'del-faq/(?P<id>[\w-]+)',
        FAQDeleteView.as_view(),
        name='delete_faq'
    ),
    url(
        r'create-rep/$',
        create_rep,
        name='create_rep'
    ),
    url(
        r'save-rep/$',
        save_rep,
        name='save_rep'
    ),
    url(
        r'del-rep/(?P<id>[\w-]+)',
        RepairDeleteView.as_view(),
        name='delete_rep'
    ),
    url(
        r'save-photo/$',
        SavePhotoView.as_view(),
        name='delete_rep'
    ),
    url(
        r'delete-photo/(?P<id>[\w-]+)',
        DeletePhotoView.as_view(),
        name='delete_photo'
    ),
]
