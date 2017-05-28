# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import View

from common.mixins import DeleteAjaxMixin
from users.forms import UserChangeForm, UserCreationForm
from users.models import User


class AdminsView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'users/admins.html'
    context_object_name = 'admins'


class AdminDetail(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'admin'
    pk_url_kwarg = 'id'
    form_class = UserChangeForm

    def get_form(self, form_class=None):
        return self.form_class(request_user=self.request.user, **self.get_form_kwargs())

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.id != int(kwargs.get('id')):
            return redirect('admin2:main')
        return super(AdminDetail, self).get(request, *args, **kwargs)


class AdminCreate(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserCreationForm


class AdminDeleteView(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = User
    pk_url_kwarg = 'id'


class ChangePass(LoginRequiredMixin, View):
    status_404 = 404

    def post(self, *args, **kwargs):
        messages = self._validate_pass(self.request)
        if messages:
            message = messages.get('message')
            status = messages.get('status')
            return HttpResponse(status=status, content=message)
        else:
            if self._set_pass(self._get_pass()):
                return HttpResponse(status=200, content='Пароль сохранен')
            return HttpResponse(status=500)

    def _get_user(self):
        admin_id = self.request.POST.get('admin')
        if admin_id:
            return get_object_or_404(User, id=admin_id)

    def _get_pass(self):
        return self.request.POST.get('pass')

    def _validate_pass(self, request):
        pass1 = request.POST.get('pass')
        pass2 = request.POST.get('pass2')
        if not pass1:
            return {"message": "Не вибран пароль", "status": self.status_404}
        elif not pass2:
            return {"message": "Нет подтверждения пароля", "status": self.status_404}
        elif pass1 != pass2:
            return {"message": "Пароли не совпадают", "status": self.status_404}

    def _set_pass(self, pass1):
        user = self._get_user()
        user.set_password(pass1)
        user.save()
        return True
