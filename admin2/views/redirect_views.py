# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admin2.forms import RedirectForm


class RedrectList(ListView):
    model = Redirect
    template_name = 'admin2/redirect/redirect_list.html'


class RedirectCreate(CreateView):
    model = Redirect
    template_name = 'admin2/redirect/redirect_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:redirect_edit', args=[self.object.id])


class RedirectEdit(UpdateView):
    model = Redirect
    template_name = 'admin2/redirect/redirect_edit.html'
    pk_url_kwarg = 'pk'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:redirect_edit', args=[self.object.id])


class RedirectDelete(DeleteView):
    model = Redirect
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:redirects'))
