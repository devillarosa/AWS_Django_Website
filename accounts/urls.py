from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views
from .api.views import UserCreateView

urlpatterns = [

    # /login
    url(r'login/$', views.login, name='login'),

    # /api/register
    url(r'api/register$', UserCreateView.as_view(), name='login'),

   # # /api/login/
   # url(r'api/login/$', index, name='index'),

   # # /api/logout/
   # url(r'api/logout/$', index, name='index'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
