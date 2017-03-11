from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView

from common.models import Application
from common.views import DeleteAjaxMixin


class Admin2MainView(LoginRequiredMixin, ListView):
    template_name = "admin2/main.html"
    model = Application
    context_object_name = 'applications'


class DellApplication(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Application


class DellAllAplications(DellApplication):

    def delete(self, request, *args, **kwargs):
        self.model.objects.all().delete()
        return HttpResponse(status=200)
