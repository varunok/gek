from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, TemplateView


class Admin2MainView(LoginRequiredMixin, TemplateView):
    template_name = "admin2/main.html"
