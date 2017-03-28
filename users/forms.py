# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField

from users.models import User


class AuthForm(AuthenticationForm):
    remember = forms.BooleanField(label='Запомнить меня', required=False,
                                  initial=False)


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput
#     )
#     password2 = forms.CharField(
#         label='Подтверждение',
#         widget=forms.PasswordInput
#     )
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Пароль и подтверждение не совпадают')
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         print (user.__dict__)
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ('email', 'group')
