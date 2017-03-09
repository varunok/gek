from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import FormView, ListView, TemplateView, DeleteView

from common.models import Application


class Admin2MainView(LoginRequiredMixin, ListView):
    template_name = "admin2/main.html"
    model = Application
    context_object_name = 'applications'


class DellApplication(LoginRequiredMixin, DeleteView):
    model = Application

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)


class DellAllAplications(DellApplication):

    def delete(self, request, *args, **kwargs):
        self.model.objects.all().delete()
        return HttpResponse(status=200)
