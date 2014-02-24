from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#url(r'^accounts/', include('auth_urls')),

urlpatterns = patterns('',
    url(r'^spellweb/', include('spellweb.urls', namespace="spellweb")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
