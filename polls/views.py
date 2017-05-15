# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from polls.models import Polls, Question
from seo.mixins import SEOMixin


class TestList(SEOMixin, ListView):
    model = Polls
    template_name = 'polls/tests.html'


class StartTest(SEOMixin, DetailView):
    model = Polls
    template_name = 'polls/test_passing.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context  = super(StartTest, self).get_context_data(**kwargs)
        if self.kwargs.get('pk_q'):
            try:
                context['question'] = Question.objects.get(id=self.kwargs.get('pk_q'))
                self.template_name = 'polls/include/question.html'
            except ObjectDoesNotExist:
                pass
        else:
            context['question'] = self.object.questions.first()
        try:
            context['next_question'] = self.object.questions.filter(id__gt=context['question'].id).first().id
        except AttributeError:
            context['next_question'] = 0
        return context


class ResultTest(SEOMixin, DetailView):
    model = Polls
    template_name = 'polls/test_result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultTest, self).get_context_data(**kwargs)
        result = int(self.kwargs.get('result'))
        self.object.test_end += 1
        self.object.save()
        context['result'] = self.object.results.filter(ball_from__lte=result, ball_to__gte=result ).first()
        context['ball'] = result
        return context

