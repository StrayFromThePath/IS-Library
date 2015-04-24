__author__ = 'User'
from django.conf.urls import patterns, include, url
from readers import views



urlpatterns = patterns('',

    # Student
    url(r'^student/new/$', views.CreateStudent.as_view(), name='new-student'),
    url(r'^student/update/(?P<pk>[0-9]+)/$', views.UpdateStudent.as_view(), name='update-student'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', views.DeleteStudent.as_view(), name='delete-student'),
    # Staff
    url(r'^staff/new/$', views.CreateStaff.as_view(), name='new-staff'),
    url(r'^staff/update/(?P<pk>[0-9]+)/$', views.UpdateStaff.as_view(), name='update-staff'),
    url(r'^staff/delete/(?P<pk>[0-9]+)/$', views.DeleteStaff.as_view(), name='delete-staff'),
    # OnceOnly
    url(r'^once/new/$', views.CreateOnceOnly.as_view(), name='new-once'),
    url(r'^once/update/(?P<pk>[0-9]+)/$', views.UpdateOnceOnly.as_view(), name='update-once'),
    url(r'^once/delete/(?P<pk>[0-9]+)/$', views.DeleteOnceOnly.as_view(), name='delete-once'),

    url(r'^page/(\d+)/$', views.readers_all),
    url(r'^$', views.readers_all, name='all-readers'),
)