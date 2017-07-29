# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.landing_views import LandingList, LandingEdit, LandingEditSeo, LandingEditForm, LandingCreate, \
    LandingDelete, LandingFutorList, LandingFutorAdd, LandingFutorDelete

urlpatterns = [
    # landing
    url(
        '^landings/$',
        LandingList.as_view(),
        name='landings'
    ),
    url(
        '^landings/edit/(?P<pk>[\d-]+)/$',
        LandingEdit.as_view(),
        name='landing_edit'
    ),
    url(
        '^landings/edit/(?P<pk>[\d-]+)/seo/$',
        LandingEditSeo.as_view(),
        name='landing_edit_seo'
    ),
    url(
        '^landings/edit/(?P<pk>[\d-]+)/form/$',
        LandingEditForm.as_view(),
        name='landing_edit_form'
    ),
    url(
        '^landings/create/$',
        LandingCreate.as_view(),
        name='landing_create'
    ),
    url(
        '^landings/delete/(?P<pk>[\d-]+)/$',
        LandingDelete.as_view(),
        name='landing_delete'
    ),
    url(
        '^landingsfutor/delete/(?P<pk>[\d-]+)/$',
        LandingFutorDelete.as_view(),
        name='landing_futor_delete'
    ),
    url(
        '^landings-futor/$',
        LandingFutorList.as_view(),
        name='landing_futor_list'
    ),
    url(
        '^landings-futor/add$',
        LandingFutorAdd.as_view(),
        name='landing_futor_add'
    ),
]