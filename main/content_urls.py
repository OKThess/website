from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /about/
    url(r'^about/$', views.about, name='about'),

    # /program/
    url(r'^program/$', views.program_redir, name='program_redir'),
    url(r'^program/teams/$', views.program_teams, name='program_teams'),
    url(r'^program/mentors/$', views.program_mentors, name='program_mentors'),
    url(r'^program/okthess-team/$', views.program_partners, name='program_partners'),
    url(r'^program/alumni/$', views.program_alumni, name='program_alumni'),

    # /meetup/
    url(r'^meetup/$', views.meetup, name='meetup'),

    # /events/
    url(r'^events/$', views.events, name='events'),

    # /weekends/
    url(r'^weekends/$', views.weekends, name='weekends'),

    # /blog/
    url(r'^blog/$', views.blog, name='blog'),

    # /resources/
    url(r'^resources/$', views.resources, name='resources'),

    # e.g. /blog/sample-post
    url(r'^blog/(?P<post_slug>[^/]*)/$', views.blog_post, name='blog_post'),

    # e.g. /blog/archives/2016/3
    url(r'^blog/archives/(?P<archive_year>[^/]*)/(?P<archive_month>[^/]*)/$', views.blog_archives, name='blog_archives'),

    # /contact/
    url(r'^contact/$', views.contact, name='contact'),

    # /apply/
    url(r'^apply/$', views.apply, name='apply'),

    # /demoday/
    url(r'^demoday/$', views.demoday, name='demoday'),
]
