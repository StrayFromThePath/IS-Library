from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library_vyz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^select2/', include('select2.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('books.urls')),
    url(r'^', include('readers.urls')),
)
