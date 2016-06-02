# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from apps.hello.models import Person
from apps.hello.models import Request


def person_list_view(request):
    """
    View for main page
    """
    person = Person.objects.first()
    return render_to_response('hello/index.html', {'person': person})


def requests_list_view(request):
    """
    View for request page
    """
    req_list = Request.objects.order_by('date_time')[:10]
    return render_to_response('hello/requests.html', {'requests': req_list})
