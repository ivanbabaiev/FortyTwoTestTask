#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Request


class RequestsMiddleware(object):
    """
    Request process_response
    """
    def process_response(self, request, response):
        if request.is_ajax():
            return response
        Request.objects.create(path=request.path,
                               server_protocol=request.META['SERVER_PROTOCOL'],
                               request_method=request.META['REQUEST_METHOD'],
                               status_code=response.status_code)
        return response
