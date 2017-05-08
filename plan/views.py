# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, UpdateView

from admin2.forms import PreparationsSet, ProcessSet, FinishSet
from plan.forms import PlanTitleForm
from plan.models import PlanPage, SaleBuildPlan, BuyBuildPlan, RentBuildPlan, PassBuildPlan, RepairBuildPlan


class PlanSitePage(DetailView):
    model = PlanPage
    template_name = 'plan/plan.html'

    def get_object(self, queryset=None):
        return self.model.get_solo()


class PlanCreatePage(TemplateView):
    template_name = 'plan/process.html'

    def get_context_data(self, **kwargs):
        context = super(PlanCreatePage, self).get_context_data(**kwargs)
        context['title_form'] = PlanTitleForm()
        context['form__preparations'] = PreparationsSet()
        context['form__process'] = ProcessSet()
        context['form__finish'] = FinishSet()
        return context


class PlanDonePage(UpdateView):
    model = PlanPage
    template_name = 'plan/final.html'
    fields = '__all__'
    success_url = reverse_lazy('plan:plan_done')

    def get_object(self, queryset=None):
        return self.model.get_solo()

    def post(self, request, *args, **kwargs):
        self.object = None
        form_list = PlanTitleForm(self.request.POST)
        form__preparations = PreparationsSet(self.request.POST)
        form__process = ProcessSet(self.request.POST)
        form__finish = FinishSet(self.request.POST)
        return self.render_to_response(
            self.get_context_data(
                form__preparations=form__preparations,
                form__process=form__process,
                form__finish=form__finish,
                form_list=form_list))



def get_plan(request, plan):
    pl = None
    data = {
        'img': None,
        'title': None,
        'forms': None
    }
    if plan == '0':
        return HttpResponse()
    elif plan == '1':
        pl = SaleBuildPlan.get_solo()
    elif plan == '2':
        pl = BuyBuildPlan.get_solo()
    elif plan == '3':
        pl = RentBuildPlan.get_solo()
    elif plan == '4':
        pl = PassBuildPlan.get_solo()
    elif plan == '5':
        pl = RepairBuildPlan.get_solo()
    if pl.image:
        data['img'] = pl.image.url
    template_formset = 'plan/forms/formset.html'
    form__preparations = PreparationsSet(instance=pl)
    form__process = ProcessSet(instance=pl)
    form__finish = FinishSet(instance=pl)
    data['form_preparations'] = render_to_string(template_formset, {'formset': form__preparations, 'iden': 'preparations'})
    data['form__process'] = render_to_string(template_formset, {'formset': form__process, 'iden': 'processes'})
    data['form__finish'] = render_to_string(template_formset, {'formset': form__finish, 'iden': 'finish'})
    data['title'] = pl.title
    data = JsonResponse(data)
    return HttpResponse(data)
