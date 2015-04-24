__author__ = 'User'
from django.conf.urls import patterns, include, url
from books import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^service/(?P<service_id>\d+)/$', views.more, name='more'),
    url(r'^all/$', views.ListBookView.as_view(), name='book-list'),
    url(r'^book/new/$', views.CreateBook.as_view(), name='new-book'),
    url(r'^book/update/(?P<pk>[0-9]+)/$', views.UpdateBook.as_view(), name='update-book'),
    url(r'^book/delete/(?P<pk>[0-9]+)/$', views.DeleteBook.as_view(), name='delete-book'),

    url(r'^booklend/new/$', views.CreateBookLend.as_view(), name='new-booklend'),
    url(r'^booklend/update/(?P<pk>[0-9]+)/$', views.UpdateBookLend.as_view(), name='update-booklend'),
    url(r'^booklend/all/$', views.ListBookLendView.as_view(), name='booklend-list'),

    url(r'^section/all/$', views.ListSectionView.as_view(), name='all-section'),
    url(r'^section/new/$', views.CreateSection.as_view(), name='new-section'),
    url(r'^section/update/(?P<pk>[0-9]+)/$', views.UpdateSection.as_view(), name='update-section'),
    url(r'^section/delete/(?P<pk>[0-9]+)/$', views.DeleteSection.as_view(), name='delete-section'),
)
