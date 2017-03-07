# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):
    remember = forms.BooleanField(label='Запомнить меня', required=False,
                                  initial=False)
