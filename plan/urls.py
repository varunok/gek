# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from plan.views import PlanSitePage, PlanCreatePage, get_plan, PlanDonePage

urlpatterns = [
    # plans
    url('^$', PlanSitePage.as_view(), name='plan'),
    url('^create/$', PlanCreatePage.as_view(), name='plan_create'),
    url('^done/$', PlanDonePage.as_view(), name='plan_done'),
    url('get-plan/(?P<plan>[\w-]+)$', get_plan, name='get_plan'),
]