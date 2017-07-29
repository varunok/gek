# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views.notes_views import NotesListView, NotesCreateView, NotesDeleteView

urlpatterns = [
    # notes view
    url('^notes/$', NotesListView.as_view(), name='notes'),
    url('^notes/create/$', NotesCreateView.as_view(), name='notes_create'),
    url('^notes/delete/(?P<pk>[\d-]+)/$', NotesDeleteView.as_view(),name='notes_delete'),
]