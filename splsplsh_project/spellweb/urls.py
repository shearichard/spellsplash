from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

from spellweb import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
