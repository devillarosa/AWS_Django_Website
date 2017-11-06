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
        url(r'^login/$', views.login_user , name='login'),

        # logout user
        url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

        # register user
        url(r'^register/$', views.register, name='register'),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
