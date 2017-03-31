from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import FormView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from users.forms import AuthForm
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login, logout)
# Create your views here.


class Admin2MainView(LoginRequiredMixin, TemplateView):
    template_name = "admin2/loginww.html"


@method_decorator(sensitive_post_parameters(), name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class LoginView(FormView):
    template_name = 'admin2/login.html'
    form_class = AuthForm
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_authenticated_user = False
    extra_context = None

    def get_context_data(self, **kwargs):
        if self.redirect_field_name not in kwargs:
            kwargs[self.redirect_field_name] = self.get_redirect_url()
        if self.extra_context is not None:
            kwargs.update(self.extra_context)

        current_site = get_current_site(self.request)
        return super(LoginView, self).get_context_data(
            site=current_site,
            site_name=current_site.name,
            **kwargs
        )

    def get_redirect_url(self):
        return self.request.POST.get(self.redirect_field_name, '') \
            or self.request.GET.get(self.redirect_field_name, '')

    def get_safe_redirect_url(self, url=None):
        if url is None:
            url = self.get_redirect_url()
        if is_safe_url(url, self.request.get_host()):
            return url
        return resolve_url(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and request.user.is_authenticated:
            redirect_to = self.get_safe_redirect_url()
            if redirect_to == request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_safe_redirect_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form),
                                       status=400)


class LoginRememberView(LoginView):
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if not form.cleaned_data['remember']:
            self.request.session.set_expiry(0)
        return HttpResponseRedirect(self.get_safe_redirect_url())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/admin/')
