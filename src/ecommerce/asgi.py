"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from .settings import base


SETTINGS_FILE = "local"

if not base.DEBUG:
    SETTINGS_FILE = "production"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"ecommerce.settings.{SETTINGS_FILE}")

application = get_asgi_application()
