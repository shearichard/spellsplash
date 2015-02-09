"""
WSGI config for splsplsh_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
sys.stdout = sys.stderr

if 'DYNO' in os.environ:
    debug = False
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splsplsh_project.splsplsh_project.settings.heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "splsplsh_project.settings.local")
    debug = True

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
import pprint
print "1" * 50
pprint.pprint(sys.path)
print "2" * 50
print root_dir
print "3" * 50
os.path.dirname(os.path.realpath(__file__))
print "4" * 50

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
#TEST LOGGING STARTS
import logging
logger = logging.getLogger('testlogger')
logger.info('This is a simple log message')
#TEST LOGGING ENDS   

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

