from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

from spellweb import views
urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'lcHIDE/$', views.MyViewLearner.as_view(), name='learnercreateHIDE'),
    url(r'lcHIDETHISTOO/$', views.LearnerCreate.as_view(), name='anamedurlHIDETHISTOO'),
    url(r'lc/', views.LearnerCreate.as_view(), name='anamedurl'),
)
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
