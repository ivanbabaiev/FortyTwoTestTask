# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from apps.hello.models import Person


def person_list_view(request):

    try:
        data = Person.objects.all()[0]
        return render_to_response('hello/index.html', {'person': data})
    except:
        return render_to_response('hello/index.html')
