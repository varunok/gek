# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from articles.views import ArticlesSiteView

urlpatterns = [
    url('^$', ArticlesSiteView.as_view(), name='articles'),
]