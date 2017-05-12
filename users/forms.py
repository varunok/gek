# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField, UserChangeForm
from django.forms.widgets import Select
from django.utils.datetime_safe import datetime

from users.models import User


class Group:
    SA = 1
    AD = 2
    CHOICES = (
        (SA, 'Супер администратор'),
        (AD, 'Администратор')
    )


class AuthForm(AuthenticationForm):
    remember = forms.BooleanField(label='Запомнить меня', required=False,
                                  initial=False)


class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput(attrs={'type': 'hidden'}),
        required=False
    )
    date_joined = forms.DateTimeField(required=False)
    group = forms.IntegerField(
        widget=Select(choices=Group.CHOICES),
        disabled=True,
        label='Група'
    )

    class Meta:
        model = User
        exclude = ['is_active', 'is_superuser', 'is_staff']
        fields = '__all__'

    def __init__(self, request_user, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        if request_user.is_superuser:
            self.fields['group'].disabled = False



class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control col-md-5 col-xs-12'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control col-md-5 col-xs-12'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    date_joined = forms.DateTimeField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.date_joined = datetime.now()
        user.is_active = True
        if commit:
            user.save()
        return user
