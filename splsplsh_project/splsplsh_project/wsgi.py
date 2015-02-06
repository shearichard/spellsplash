"""
WSGI config for splsplsh_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splsplsh_project.settings.local")
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print root_dir
print ""
import pprint
pprint.pprint(sys.path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
