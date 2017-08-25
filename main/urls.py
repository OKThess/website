from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = 'main'
admin.site.site_header = 'OK!Thess administration'
urlpatterns = [
    # /
    url(r'^$', views.get_index, name='index'),

    # /about/
    url(r'^about/$', views.get_about, name='about'),
    # /program/
    url(r'^program/$', views.get_program, name='program'),
    # /events/
    url(r'^events/$', views.get_events, name='events'),
    # /blog/
    url(r'^blog/$', views.get_blog, name='blog'),
    # e.g. /blog/sample-post
    url(r'^blog/sample-post/$', views.get_blog_post_sample, name='post'),
    # /contact/
    url(r'^contact/$', views.get_contact, name='contact'),

    # /apply/
    url(r'^apply/$', views.apply, name='apply'),
]
