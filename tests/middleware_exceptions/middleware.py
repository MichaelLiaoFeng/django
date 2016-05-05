from __future__ import unicode_literals

from django.core.handlers.middleware import MiddlewareMixin
from django.http import HttpResponse


class ProcessExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        return HttpResponse('Exception caught')
