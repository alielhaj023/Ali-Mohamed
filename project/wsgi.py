"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = SentryWsgiMiddleware(get_wsgi_application())
