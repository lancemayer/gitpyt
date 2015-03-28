from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'createrepository.views.index', name='index'),
    url(r'^new/$', 'createrepository.views.createNewRepository', name='createNewRepository'),
)
