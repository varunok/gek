# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from admin2.models import SettingsFranchise
from privat24.models import Privat24Transaction


class PayListForm(forms.ModelForm):

    class Meta:
        model = SettingsFranchise
        fields = '__all__'


# class ConfirmPayForm(forms.Form):
#     merchant = forms.ModelForm

class Privat24TransactionForm(forms.ModelForm):
    class Meta:
        model = Privat24Transaction
        fields = '__all__'
        exclude = 'signature',