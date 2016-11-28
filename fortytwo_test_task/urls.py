from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import patterns, url
from apps.hello.views import RequestsViewList, requests_list_json

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^$', index, name='index'),
    url(r'^$', include('apps.hello.urls'), name="hello"),
    url(r'^requests$', RequestsViewList.as_view(), name='requests'),
    url(r'^requests_json$', requests_list_json, name='ajax_requests'),

    url(r'^admin/', include(admin.site.urls), name="admin"),

)
