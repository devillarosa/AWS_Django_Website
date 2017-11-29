from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls')),
    url(r'^', include('fitness.urls')),
]
