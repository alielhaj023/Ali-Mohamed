from __future__ import annotations

import sentry_sdk
from django.utils.deprecation import MiddlewareMixin


class SentryMiddleware(MiddlewareMixin):
    """
    Middleware to capture errors and attach extra request data to Sentry.
    """

    def process_exception(self, request, exception):
        """
        Captures exceptions and sends them to Sentry.
        """
        sentry_sdk.capture_exception(exception)

    def process_request(self, request):
        """
        Attaches user and request metadata to Sentry.
        """
        with sentry_sdk.configure_scope() as scope:
            if request.user.is_authenticated:
                scope.set_user(
                    {
                        "id": request.user.id,
                        "email": request.user.email,
                        "username": request.user.username,
                    }
                )
            scope.set_extra("method", request.method)
            scope.set_extra("path", request.path)
            scope.set_extra("GET_params", request.GET)
            scope.set_extra("POST_params", request.POST)


class SentryPerformanceMiddleware(MiddlewareMixin):
    """
    Middleware to capture performance traces using Sentry.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Start a performance transaction.
        """
        transaction_name = f"{request.method} {request.path}"
        sentry_sdk.set_transaction_name(transaction_name)

    def process_response(self, request, response):
        """
        End the performance transaction.
        """
        sentry_sdk.set_tag("http.status_code", response.status_code)
        return response
