from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin


class DeleteAjaxMixin(SingleObjectMixin):

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)