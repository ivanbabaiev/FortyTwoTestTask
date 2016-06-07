# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from apps.hello.models import Person
from apps.hello.models import Request


def person_list_view(request):
    """
    View for main page
    """
    person = Person.objects.first()
    return render_to_response('hello/index.html', {'person': person})


class RequestsViewList(TemplateView):
    """
    View for request page
    """
    template_name = "hello/requests.html"

    def get_context_data(self, **kwargs):
        request_list = Request.objects.order_by('-date_time')[:10]
        context = super(RequestsViewList, self).get_context_data(**kwargs)
        context['title'] = 'Requests'
        context['requests'] = request_list
        return context


def requests_list_json(request):
    """
    Request json list
    """
    read_requests = Request.objects.filter(viewed=False)

    if 'window_state' in request.GET.keys():
        if request.GET['window_state'] == 'active':
            read_requests.update(viewed=True)
    request_new_title = "(%i) Requests on list" % (len(read_requests))
    response_data = {}
    request_list = Request.objects.order_by('-date_time')[:10]
    ajax_request_list = [req.__str__() for req in request_list]
    response_data['requests_title'] = request_new_title
    response_data['requests_list'] = ajax_request_list
    response = HttpResponse(json.dumps(response_data),
                            content_type="application/json")
    return response
