# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from liqpayapp.models import LiqPayTransaction


class LiqPayTransactionForm(forms.ModelForm):
    class Meta:
        model = LiqPayTransaction
        fields = '__all__'