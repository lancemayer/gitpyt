from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'gitpyt.views.index', name='index'),
    url(r'^login/$', 'gitpyt.views.loginPage', name='loginPage'),
    url(r'^authenticate/$', 'gitpyt.views.authenticateUser', name='authenticateUser'),
    url(r'^logout/$', 'gitpyt.views.logoutUser', name='logoutUser'),
    url(r'^signup/$', 'gitpyt.views.signup', name='signup'),
    url(r'^createrepository/', include('createrepository.urls', namespace='createrepository')),
    url(r'^admin/', include(admin.site.urls)),
]
