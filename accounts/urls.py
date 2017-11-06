from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views
from .api.views import UserCreateView, UserLoginView
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

        # Home page for logging in
        url(r'^$', views.loginPage, name='loginPage'),

        # login user
        url(r'^login_user/$', views.login_user , name='login_user'),

        # register new user
        url(r'^api/user/$', UserCreateView.as_view(), name='rest_register'),

        ]

urlpatterns = format_suffix_patterns(urlpatterns)
