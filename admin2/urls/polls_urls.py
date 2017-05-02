# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from admin2.views import polls_views

urlpatterns = [
    # POLLS
    url(r'^polls/$',polls_views.PollsList.as_view(),name='polls'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/$', polls_views.PollEdit.as_view(),name='poll_edit'),
    url(r'^polls/delete/(?P<pk>[\w-]+)/$', polls_views.DeletePoll.as_view(),name='poll_delete'),
    url(r'^polls/create/$', polls_views.PollCreate.as_view(),name='poll_create'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/$', polls_views.PollQuestionEdit.as_view(),name='poll_edit_question'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/results/$', polls_views.ResultList.as_view(),name='poll_results'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/create/$', polls_views.PollQuestionCreate.as_view(),name='poll_create_question'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/results/create/$', polls_views.ResultCreate.as_view(),name='poll_create_results'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/edit/(?P<pk_m>[\w-]+)/$', polls_views.QuestionEdit.as_view(),name='edit_question'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/delete/(?P<pk_m>[\w-]+)/$', polls_views.QuestionDelete.as_view(),name='delete_question'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/results/edit/(?P<pk_r>[\w-]+)/$', polls_views.ResultEdit.as_view(),name='edit_result'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/results/delete/(?P<pk_r>[\w-]+)/$', polls_views.ResultDelete.as_view(),name='delete_result'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/edit/(?P<pk_m>[\w-]+)/choices/$', polls_views.Choices.as_view(),name='choices_list'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/edit/(?P<pk_m>[\w-]+)/choices/edit/(?P<pk_c>[\w-]+)/$', polls_views.ChoicesEdit.as_view(),name='edit_choices'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/edit/(?P<pk_m>[\w-]+)/choices/delete/(?P<pk_c>[\w-]+)/$', polls_views.ChoicesDelete.as_view(),name='delete_choices'),
    url(r'^polls/edit/(?P<pk>[\w-]+)/questions/edit/(?P<pk_m>[\w-]+)/choices/create/$', polls_views.ChoicesCreate.as_view(),name='create_choices'),
    ]