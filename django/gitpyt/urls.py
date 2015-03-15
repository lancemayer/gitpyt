from django.conf.urls import patterns, include, url
from django.contrib import admin

# from gitpyt import views

urlpatterns = patterns('',
    url(r'^$', 'gitpyt.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
