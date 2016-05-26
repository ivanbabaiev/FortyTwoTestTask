#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url

from apps.hello.views import person_list_view

urlpatterns = patterns(
    '',
    url(r'^$', person_list_view, name='home'),

)

urlpatterns += staticfiles_urlpatterns()
