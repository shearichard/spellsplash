import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


#The remainder of this file is derived from 
#https://devcenter.heroku.com/articles/getting-started-with-django#django-settings
#

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/app/splsplsh_project/staticfiles')
#STATIC_URL = '/static/'
#
#STATICFILES_DIRS = (
#    normpath(join(SITE_ROOT, 'assets')),
#)
#print "HERO" * 10
#print BASE_DIR
#print 'SITE_ROOT : ' + SITE_ROOT
#print 'STATIC_ROOT : ' + STATIC_ROOT
#print 'STATIC_URL : ' + STATIC_URL 
#print 'STATICFILES_DIRS : ' + STATICFILES_DIRS
#print "HERO" * 10
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django_pdb.middleware.PdbMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'splsplsh_project.splsplsh_project.middleware.LoginRequiredMiddleware',
)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
