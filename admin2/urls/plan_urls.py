# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.urls import reverse_lazy

from admin2.forms import PreparationsSet, ProcessSet, FinishSet
from admin2.views.plan_views import PlanView, GalleryPlanView, TemplatesPlanView, EditPlanTemplates, \
    EditPlansItem
from plan.models import SaleBuildPlan, BuyBuildPlan, RentBuildPlan, PassBuildPlan, RepairBuildPlan

urlpatterns = [
    # plan
    url('^plan/$', PlanView.as_view(), name='plan'),
    url('^plan/gallery/$', GalleryPlanView.as_view(), name='plan_gallery'),
    url('^plan/templates/$', TemplatesPlanView.as_view(), name='plan_templates'),

    url('^plan/templates/sale-build-plan/$', EditPlanTemplates.as_view(model=SaleBuildPlan),name='sale_build_plan'),
    url('^plan/templates/sale-build-plan/plans/$', EditPlansItem.as_view(model=SaleBuildPlan), name='sale_build_items_plan'),

    url('^plan/templates/buy-build-plan/$', EditPlanTemplates.as_view(model=BuyBuildPlan),name='buy_build_plan'),
    url('^plan/templates/buy-build-plan/plans/$', EditPlansItem.as_view(model=BuyBuildPlan), name='buy_build_items_plan'),

    url('^plan/templates/rent-build-plan/$', EditPlanTemplates.as_view(model=RentBuildPlan),name='rent_build_plan'),
    url('^plan/templates/rent-build-plan/plans/$', EditPlansItem.as_view(model=RentBuildPlan), name='rent_build_items_plan'),

    url('^plan/templates/pass-build-plan/$', EditPlanTemplates.as_view(model=PassBuildPlan),name='pass_build_plan'),
    url('^plan/templates/pass-build-plan/plans/$', EditPlansItem.as_view(model=PassBuildPlan), name='pass_build_items_plan'),

    url('^plan/templates/repair-build-plan/$', EditPlanTemplates.as_view(model=RepairBuildPlan),name='repair_build_plan'),
    url('^plan/templates/repair-build-plan/plans/$', EditPlansItem.as_view(model=RepairBuildPlan), name='repair_build_items_plan'),

]

