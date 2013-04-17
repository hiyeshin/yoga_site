"""
WSGI configuration for rpi_ws project
This module contains the WSGI application used by Django's development server
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pi_io.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# apply WSGI middleware here below