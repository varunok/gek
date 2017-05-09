# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from admin2.models import SettingsFranchise


class PayListForm(forms.ModelForm):

    class Meta:
        model = SettingsFranchise
        fields = '__all__'


# class ConfirmPayForm(forms.Form):
#     merchant = forms.ModelForm