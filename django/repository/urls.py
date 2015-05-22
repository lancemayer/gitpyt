from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<repoName>.+)$', 'repository.views.index', name='index'),
]
