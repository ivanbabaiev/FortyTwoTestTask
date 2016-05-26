from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import patterns, url

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^$', index, name='index'),
    url(r'^$', include('apps.hello.urls')),

    url(r'^admin/', include(admin.site.urls), name="admin"),

)
