from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import patterns, url
from apps.hello.views import requests_list_view

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^$', index, name='index'),
    url(r'^$', include('apps.hello.urls'), name="hello"),
    url(r'^requests/', requests_list_view, name="requests"),

    url(r'^admin/', include(admin.site.urls), name="admin"),

)
