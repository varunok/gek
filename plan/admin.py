# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solo.admin import SingletonModelAdmin

from common.admin import PhotoInline, ProcessInline, PreparationInline, FinishInline
from plan.models import PlanPage, SaleBuildPlan

class PlanPageAdmin(SingletonModelAdmin):
    inlines = [PhotoInline]

class SaleBuildPlanAdmin(SingletonModelAdmin):
    inlines = [PreparationInline, FinishInline, ProcessInline]

admin.site.register(PlanPage, PlanPageAdmin)
admin.site.register(SaleBuildPlan, SaleBuildPlanAdmin)
