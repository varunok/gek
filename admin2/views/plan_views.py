# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import ContextMixin, TemplateView

from admin2.forms import PreparationsSet, ProcessSet, FinishSet
from common.mixins import FormSetMixin
from common.models import Preparation
from plan.models import PlanPage, SaleBuildPlan, BuyBuildPlan, RentBuildPlan, PassBuildPlan, RepairBuildPlan


class PlanMixin(ContextMixin):
    model = None
    prefix = None
    nav = None

    def get_context_data(self, **kwargs):
        context = super(PlanMixin, self).get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        context['prefix'] = self.prefix
        context['nav'] = self.nav
        try:
            context['object'] = self.get_object()
        except AttributeError:
            pass
        return context

class PlanView(PlanMixin, UpdateView):
    model = PlanPage
    template_name = 'admin2/plan/plan_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:plan')

    def get_object(self, queryset=None):
        return PlanPage.get_solo()


class GalleryPlanView(PlanView):
    template_name = 'admin2/plan/plan_gallery.html'


class TemplatesPlanView(PlanMixin, TemplateView):
    model = PlanPage
    template_name = 'admin2/plan/plan_templates.html'

    def get_context_data(self, **kwargs):
        context = super(TemplatesPlanView, self).get_context_data(**kwargs)
        context['salebuildplan'] = SaleBuildPlan.get_solo()
        context['buybuildplan'] = BuyBuildPlan.get_solo()
        context['rentbuildplan'] = RentBuildPlan.get_solo()
        context['passbuildplan'] = PassBuildPlan.get_solo()
        context['repairbuildplan'] = RepairBuildPlan.get_solo()
        return context

    def get_object(self, queryset=None):
        return PlanPage.get_solo()


class EditPlanTemplates(PlanMixin, UpdateView):
    fields = '__all__'
    template_name = 'admin2/plan/plan_templates_edit.html'

    def get_object(self, queryset=None):
        model_name = self.model.__name__
        temp_nav = 'admin2/plan/navs/{0}_build_nav.html'
        if model_name == 'SaleBuildPlan':
            self.nav = render_to_string(temp_nav.format('sale'))
        elif model_name == 'BuyBuildPlan':
            self.nav = render_to_string(temp_nav.format('buy'))
        elif model_name == 'RentBuildPlan':
            self.nav = render_to_string(temp_nav.format('rent'))
        elif model_name == 'PassBuildPlan':
            self.nav = render_to_string(temp_nav.format('pass'))
        elif model_name == 'RepairBuildPlan':
            self.nav = render_to_string(temp_nav.format('repair'))
        return self.model.get_solo()


class EditPlansItem(PlanMixin, FormSetMixin):
    fields = '__all__'
    template_name = 'admin2/plan/plan_templates_preparations.html'

    def get_object(self, queryset=None):
        return self.model.get_solo()

    def get_formset(self, request):
        tmp_name = 'admin2/plan/navs/{0}_build_nav.html'.format(self.get_prefix_tmp__name())
        rev = 'admin2:{0}_build_items_plan'.format(self.get_prefix_tmp__name())
        self.nav = render_to_string(tmp_name, {'request':self.request})
        if 'preparations' in request.GET:
            self.formset = PreparationsSet
            self.prefix = 'preparation'
            self.success_url = reverse_lazy(rev)+'?preparations'
        elif 'process' in request.GET:
            self.formset = ProcessSet
            self.prefix = 'process'
            self.success_url = reverse_lazy(rev) + '?process'
        elif 'finish' in request.GET:
            self.formset = FinishSet
            self.prefix = 'finish'
            self.success_url = reverse_lazy(rev) + '?finish'
        return self.formset

    def get_prefix_tmp__name(self):
        model_name = self.model.__name__
        if model_name == 'SaleBuildPlan':
            return 'sale'
        elif model_name == 'BuyBuildPlan':
            return 'buy'
        elif model_name == 'RentBuildPlan':
            return 'rent'
        elif model_name == 'PassBuildPlan':
            return 'pass'
        elif model_name == 'RepairBuildPlan':
            return 'repair'



