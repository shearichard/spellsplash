from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from django.views.static import serve
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#url(r'^accounts/', include('auth_urls')),
# Provide static url without leading slash
_static_url = settings.STATIC_URL
if _static_url.startswith('/'):
        _static_url = _static_url[1:]

urlpatterns = patterns('',
    url(r'^%s(?P<path>.*)$' % _static_url, serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^$', RedirectView.as_view(url='/spellweb/')),
    url(r'^spellweb/', include('spellweb.urls', namespace="spellweb")),
    url(r'^admin/', include(admin.site.urls)),
      #override the default urls
      url(r'^accounts/password/change/$',
                    auth_views.password_change,
                    name='password_change'),
      url(r'^accounts/password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
      url(r'^accounts/password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
      url(r'^accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
      url(r'^accounts/password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
      url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='auth_password_reset_confirm'),

      #and now add the registration urls
      url(r'^accounts/', include('registration.backends.default.urls')),

)
