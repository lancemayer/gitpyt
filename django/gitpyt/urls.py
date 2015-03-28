from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'gitpyt.views.index', name='index'),
    url(r'^mkdir/$', 'gitpyt.views.mkdir', name='mkdir'),
    url(r'^createrepository/', include('createrepository.urls', namespace="createrepository")),
    url(r'^admin/', include(admin.site.urls)),
)
