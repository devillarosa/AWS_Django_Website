from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views
from .api.views import UserCreateView, UserLoginView

urlpatterns = [

        # login page
        #url(r'login/$', views.login, name='login'),

        # register new user
        url(r'^api/user/$', UserCreateView.as_view(), name='rest_register'),

        # login existing user
        url(r'^api/login/$', UserLoginView.as_view(), name='rest_register'),


        ]

urlpatterns = format_suffix_patterns(urlpatterns)
