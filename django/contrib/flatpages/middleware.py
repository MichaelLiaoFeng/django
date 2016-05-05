from django.conf import settings
from django.contrib.flatpages.views import flatpage
from django.http import Http404, HttpResponse


class FlatpageFallbackMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Http404:
            # TODO: fix
            response = HttpResponse(status=404)
        return self.process_response(request, response)

    def process_response(self, request, response):
        if response.status_code != 404:
            return response  # No need to check for a flatpage for non-404 responses.
        try:
            return flatpage(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except Exception:
            if settings.DEBUG:
                raise
            return response
