# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from polls.views import TestList, StartTest, ResultTest

urlpatterns = [
    # polls
    url('^$', TestList.as_view(), name='test'),
    url('^(?P<pk>[\w-]+)/$', StartTest.as_view(), name='test_start'),
    url('^(?P<pk>[\w-]+)/next-question/(?P<pk_q>[\w-]+)$', StartTest.as_view(), name='next_question'),
    url('^(?P<pk>[\w-]+)/get-result/(?P<result>[\w-]+)$', ResultTest.as_view(), name='get_result'),
]