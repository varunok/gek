# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.views.generic.base import ContextMixin

from seo.models import SEO


class SEOMixin(ContextMixin):
    seo_model = None
    object = None

    def get_context_data(self, **kwargs):
        context = super(SEOMixin, self).get_context_data(**kwargs)
        path = str(Site.objects.get_current()) + self.request.get_full_path()
        if SEO.objects.filter(url=path).exists():

            context['seo'] = SEO.objects.filter(url=path).first()
        else:
            try:
                context['seo'] = self.seo_model.get_solo()
            except:
                context['seo'] = self.object
        return context