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

    # main view
    url('^$', main_views.Admin2MainView.as_view(), name='main'),
    url
    (
        '^app/dell/(?P<pk>\d+)/$',
        main_views.DellApplication.as_view(),
        name='dell_app'
    ),
    url(
        '^app/dell/all/$',
        main_views.DellAllAplications.as_view(),
        name='dell_app_all'
    ),

    # sections article, articles_view
    url(
        '^articles/sections/$',
        articles_views.SectionsView.as_view(),
        name='sections'
    ),
    url(
        '^articles/sections/update/(?P<slug>[\w-]+)/$',
        articles_views.SectionsUpdateView.as_view(),
        name='sections_update'
    ),
    url(
        '^articles/sections/delete/(?P<slug>[\w-]+)/$',
        articles_views.SectionsDeleteView.as_view(),
        name='sections_delete'
    ),
    url(
        '^articles/sections/create/$',
        articles_views.SectionsCreateView.as_view(),
        name='sections_create'
    ),

    # articles, articles_view
    url(
        '^articles/articles/$',
        articles_views.ArticlesView.as_view(),
        name='articles'
    ),
    url(
        '^articles/articles/update/(?P<slug>[\w-]+)/$',
        articles_views.ArticlesUpdateView.as_view(),
        name='articles_update'
    ),
    url(
        '^articles/articles/create/$',
        articles_views.ArticlesCreateView.as_view(),
        name='articles_create'
    ),
    url(
        '^articles/articles/delete/(?P<slug>[\w-]+)/$',
        articles_views.ArticlesDeleteView.as_view(),
        name='articles_delete'
    ),

    # SETTINGS VIEW
    url(
        r'^settings/$',
        settings_views.SettingsView.as_view(),
        name='settings'
    ),

    # STATIC PAGES
    url(
        r'^static_pages/$',
        static_page_views.StaticPageView.as_view(),
        name='static_pages'
    ),
    url(
        r'^static_pages/edit/(?P<slug>[\w-]+)/$',
        static_page_views.StaticPageDetailView.as_view(),
        name='static_page_detail'
    ),
    url(
        r'status_static_page',
        static_page_views.status_page,
        name='status_static_page'
    ),

    # SERVICES
    url(
        r'^services/$',
        services_views.ServicesView.as_view(),
        name='services'
    ),
    url(
        r'status_service',
        services_views.status_service,
        name='status_service'
    ),
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
    url(
        r'^services/edit/rieltor_service/$',
        services_views.RieltorServiceView.as_view(),
        name='rieltor_service_edit'
    ),
    url(
        r'^services/edit/valuation/$',
        services_views.ValuationServiceView.as_view(),
        name='valuation_edit'
    ),
    url(
        r'^services/edit/repair/$',
        services_views.RepairServiceView.as_view(),
        name='repair_edit'
    ),
    url(
        r'^services/edit/insurence/$',
        services_views.InsurenceServiceView.as_view(),
        name='insurence_edit'
    ),
    url(
        r'^services/edit/cleaning/$',
        services_views.CleaningServiceView.as_view(),
        name='cleaning_edit'
    ),
    url(
        r'^services/edit/installation_water/$',
        services_views.InstallationWaterServiceView.as_view(),
        name='installation_water_edit'
    ),
    url(
        r'^services/edit/universal/(?P<pk>[\w-]+)/$',
        services_views.UniversalServiceView.as_view(),
        name='universal_edit'
    ),
    url(
        r'^services/create/universal/$',
        services_views.UniversalServiceCreate.as_view(),
        name='universal_create'
    ),
    url(
        '^services/delete/(?P<slug>[\w-]+)/$',
        services_views.UniversalServiceDeleteView.as_view(),
        name='sections_delete'
    ),
]
