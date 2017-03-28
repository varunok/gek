from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.generic.detail import SingleObjectMixin, BaseDetailView
from django.views.generic.list import BaseListView


class DeleteAjaxMixin(SingleObjectMixin):

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)


class ViewsCountMixin(BaseDetailView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views = F('views') + 1
        self.object.save()
        return super(ViewsCountMixin, self).get(request, *args, **kwargs)


class DinamicNextMixin(BaseListView):

    def get_context_data(self, **kwargs):
        context = super(DinamicNextMixin, self).get_context_data(**kwargs)
        count_next = self.object_list.count() - self.paginate_by
        context['count_next'] = 0 if count_next <= 0 else count_next
        return context

    def get(self, request, *args, **kwargs):
        page = self.request.GET.get('page')
        section = self.request.GET.get('section')
        if page:
            self.template_name = 'articles/include/articles_list.html'
            object_list = self.get_queryset()
            if section:
                object_list = object_list.filter(sections=section)
            paginator = self.get_paginator(object_list, self.paginate_by)
            data = JsonResponse({
                'next': paginator.page(page).has_next(),
                'articles': render_to_string(self.template_name,
                                             {'articles': paginator.page(page).object_list}),
                'obj': len(paginator.page(page).object_list)
            })
            return HttpResponse(data)
        return super(DinamicNextMixin, self).get(request, *args, **kwargs)