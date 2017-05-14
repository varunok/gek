from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DeleteView

from common.models import Application
from common.mixins import DeleteAjaxMixin


class Admin2MainView(LoginRequiredMixin, ListView):
    template_name = "admin2/main.html"
    model = Application
    context_object_name = 'applications'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        Application.objects.update(is_reading=True)
        return super(Admin2MainView, self).get(request, *args, **kwargs)


class DellApplication(LoginRequiredMixin, DeleteAjaxMixin, DeleteView):
    model = Application


class DellAllAplications(DellApplication):

    def delete(self, request, *args, **kwargs):
        self.model.objects.all().delete()
        return HttpResponse(status=200)


def check_notyfy(request):
    notify = Application.objects.filter(is_reading=False).count()
    data = JsonResponse({
        'notify': notify
    })
    return HttpResponse(data)
