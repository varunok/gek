from django.conf.urls import url

from admin2.views import login_views, main_views

urlpatterns = [
    # login views
    url('^login/$', login_views.LoginRememberView.as_view(), name='auth_login'),

    # main view
    url('^$', main_views.Admin2MainView.as_view(), name='main'),
]