# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.widgets import Select, TextInput

from common.models import Preparation
from plan.models import SaleBuildPlan, PassBuildPlan, BuyBuildPlan, RentBuildPlan, RepairBuildPlan


class PlanList(object):
    try:
        list = (
            ('0', 'Свой план'),
            ('1', SaleBuildPlan.get_solo()),
            ('2', BuyBuildPlan.get_solo()),
            ('3', RentBuildPlan.get_solo()),
            ('4', PassBuildPlan.get_solo()),
            ('5', RepairBuildPlan.get_solo()),
        )
    except:
        pass


class PlanTitleForm(forms.Form):

    list_plan = forms.CharField(
        widget=Select(choices=PlanList.list)
    )
    name = forms.CharField(
        widget=TextInput()
    )

# class FormPreparation(forms.ModelForm):
#     class Meta:
#         model = Preparation
#         fields = '__all__'
