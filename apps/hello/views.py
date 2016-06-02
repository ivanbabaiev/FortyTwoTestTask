# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from apps.hello.models import Person


def person_list_view(request):
    """
    View for main page
    """
    person = Person.objects.first()
    return render_to_response('hello/index.html', {'person': person})
