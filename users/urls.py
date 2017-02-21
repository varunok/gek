from django.conf.urls import url


# from django.contrib.auth import views as pass_reset_views
from users import views

urlpatterns = [
    url('^login/$', views.LoginRememberView.as_view(), name='auth_login'),
]
