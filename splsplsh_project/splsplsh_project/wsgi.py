"""
WSGI config for splsplsh_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

if 'DYNO' in os.environ:
    debug = False
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splsplsh_project.settings.heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splsplsh_project.settings.local")
    debug = True

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

