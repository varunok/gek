# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from polls.models import Polls, Question, URLResult
from seo.mixins import SEOMixin


class TestList(SEOMixin, ListView):
    model = Polls
    template_name = 'polls/tests.html'
    ordering = ['id']


class StartTest(SEOMixin, DetailView):
    model = Polls
    template_name = 'polls/test_passing.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(StartTest, self).get_context_data(**kwargs)
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

    def get(self, request, *args, **kwargs):
        result = int(self.kwargs.get('result'))
        polls = self.model.objects.get(id=self.kwargs.get('pk'))
        polls.test_end += 1
        polls.save()
        url_result = URLResult.objects.create(
            result=polls.results.filter(ball_from__lte=result, ball_to__gte=result).first(),
            ball=result
        )
        return HttpResponseRedirect(reverse_lazy('polls:url_result', args=[url_result.slug]))


class ResultUrl(SEOMixin, DetailView):
    model = Polls
    template_name = 'polls/test_result.html'

    def get_object(self, queryset=None):
        result = URLResult.objects.get(slug=self.kwargs.get('result')).result
        return result.polls.first()

    def get_context_data(self, **kwargs):
        context = super(ResultUrl, self).get_context_data(**kwargs)
        context['result'] = URLResult.objects.get(slug=self.kwargs.get('result')).result
        context['ball'] = URLResult.objects.get(slug=self.kwargs.get('result')).ball
        return context
