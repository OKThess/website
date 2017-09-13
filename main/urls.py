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
    url(r'^program/$', views.program_redir, name='program_redir'),
    url(r'^program/teams/$', views.get_program_teams, name='program_teams'),
    url(r'^program/mentors/$', views.get_program_mentors, name='program_mentors'),
    url(r'^program/alumni/$', views.get_program_alumni, name='program_alumni'),

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

    # /health
    url(r'^health/$', views.health, name='health'),
]
