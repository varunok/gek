# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin

from admin2.forms import QuestionForm, ChoicesForm, PollsForm
from polls.models import Polls, Question, Choice, Result


class PollsMixin(ContextMixin):
    kwargs = None
    model = None

    def get_context_data(self, **kwargs):
        context = super(PollsMixin, self).get_context_data(**kwargs)
        context['object'] = Polls.objects.get(id=self.kwargs.get('pk'))
        context['content_type'] = ContentType.objects.get_for_model(self.model).id
        try:
            context['question'] = Question.objects.get(id=self.kwargs.get('pk_m'))
        except:
            pass
        return context


class PollsList(ListView):
    model = Polls
    paginate_by = 10
    template_name = 'admin2/polls/polls_list.html'


class PollEdit(UpdateView):
    model = Polls
    template_name = 'admin2/polls/polls_edit.html'
    pk_url_kwarg = 'pk'
    form_class = PollsForm

    def get_success_url(self):
        return reverse_lazy('admin2:poll_edit', args=[self.kwargs.get('pk')])


class PollCreate(CreateView):
    model = Polls
    template_name = 'admin2/polls/polls_edit.html'
    form_class = PollsForm
    success_url = reverse_lazy('admin2:polls')


class PollQuestionEdit(PollsMixin, ListView):
    model = Question
    template_name = 'admin2/polls/question_list.html'

    def get_queryset(self):
        return self.model.objects.filter(polls__id=self.kwargs.get('pk'))


class PollQuestionCreate(PollsMixin, CreateView):
    template_name = 'admin2/polls/question_create.html'
    form_class = QuestionForm
    model = Question

    def get_success_url(self):
        return reverse_lazy('admin2:poll_edit_question', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        polls = Polls.objects.get(id=self.kwargs.get('pk'))
        self.object = form.save()
        polls.questions.add(self.object)
        polls.save()
        return super(PollQuestionCreate, self).form_valid(form)


class QuestionEdit(PollsMixin, UpdateView):
    model = Question
    template_name = 'admin2/polls/question_create.html'
    pk_url_kwarg = 'pk_m'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:poll_edit_question', args=[self.kwargs.get('pk')])


class Choices(PollsMixin, ListView):
    model = Choice
    template_name = 'admin2/polls/choices_list.html'

    def get_queryset(self):
        return self.model.objects.filter(question=Question.objects.get(id=self.kwargs.get('pk_m')))


class ChoicesEdit(PollsMixin, UpdateView):
    model = Choice
    template_name = 'admin2/polls/choices_create.html'
    form_class = ChoicesForm
    pk_url_kwarg = 'pk_c'

    def get_success_url(self):
        return reverse_lazy('admin2:choices_list', args=[self.kwargs.get('pk'), self.kwargs.get('pk_m')])


class ChoicesCreate(PollsMixin, CreateView):
    template_name = 'admin2/polls/choices_create.html'
    form_class = ChoicesForm
    model = Choice

    def get_success_url(self):
        return reverse_lazy('admin2:choices_list', args=[self.kwargs.get('pk'), self.kwargs.get('pk_m')])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.question = Question.objects.get(id=self.kwargs.get('pk_m'))
        self.object.save()
        return super(ChoicesCreate, self).form_valid(form)


class ResultList(PollsMixin, ListView):
    model = Result
    template_name = 'admin2/polls/result_list.html'

    def get_queryset(self):
        return self.model.objects.filter(polls=Polls.objects.get(id=self.kwargs.get('pk')))


class ResultEdit(PollsMixin, UpdateView):
    model = Result
    template_name = 'admin2/polls/result_edit.html'
    pk_url_kwarg = 'pk_r'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin2:edit_result', args=[self.kwargs.get('pk'), self.kwargs.get('pk_r')])


class ResultCreate(PollsMixin, CreateView):
    template_name = 'admin2/polls/result_edit.html'
    fields = '__all__'
    model = Result

    def get_success_url(self):
        return reverse_lazy('admin2:edit_result', args=[self.kwargs.get('pk'), self.object.id])

    def form_valid(self, form):
        polls = Polls.objects.get(id=self.kwargs.get('pk'))
        self.object = form.save()
        polls.results.add(self.object)
        polls.save()
        return super(ResultCreate, self).form_valid(form)


class DeletePoll(DeleteView):
    model = Polls

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:polls'))


class QuestionDelete(DeleteView):
    model = Question
    pk_url_kwarg = 'pk_m'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:poll_edit_question', args=[self.kwargs.get('pk')]))


class ChoicesDelete(DeleteView):
    model = Choice
    pk_url_kwarg = 'pk_c'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:choices_list',
                                                 args=[self.kwargs.get('pk'), self.kwargs.get('pk_m')]))


class ResultDelete(DeleteView):
    model = Result
    pk_url_kwarg = 'pk_r'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('admin2:poll_results', args=[self.kwargs.get('pk')]))

