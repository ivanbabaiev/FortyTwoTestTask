# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from apps.hello.models import Person


def person_list_view(request):

    try:
        data = get_object_or_404(Person, pk=1)
        return render_to_response('hello/index.html', {'person': data})
    except:
        return render_to_response('hello/index.html')
