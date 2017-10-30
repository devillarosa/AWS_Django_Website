from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

urlpatterns = [
    # /user/
    url(r'user/$', CreateView.as_view(), name='create'),

    # /user/id
    url(r'user/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name='details'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
