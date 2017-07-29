# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from admin2.forms import NotesForm
from admin2.models import Notes
from common.mixins import SuccesMixin, MessageMixin


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'admin2/notes/notes_list.html'
    paginate_by = 10


class NotesCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Notes
    template_name = 'admin2/notes/notes_form.html'
    form_class = NotesForm
    success_url = reverse_lazy('admin2:notes')


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    pk_url_kwarg = 'pk'
    template_name = 'admin2/common/delete_confirm.html'
    success_url = reverse_lazy('admin2:notes')
