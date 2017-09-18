from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from . import views


app_name = 'main'
admin.site.site_header = 'OK!Thess administration'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /about/
    url(r'^about/$', views.about, name='about'),

    # /program/
    url(r'^program/$', views.program_redir, name='program_redir'),
    url(r'^program/teams/$', views.program_teams, name='program_teams'),
    url(r'^program/mentors/$', views.program_mentors, name='program_mentors'),
    url(r'^program/alumni/$', views.program_alumni, name='program_alumni'),

    # /events/
    url(r'^events/$', views.events, name='events'),

    # /blog/
    url(r'^blog/$', views.blog, name='blog'),

    # e.g. /blog/sample-post
    url(r'^blog/(?P<post_id>[^/]*)/$', views.blog_post, name='blog_post'),

    # /contact/
    url(r'^contact/$', views.contact, name='contact'),

    # /apply/
    url(r'^apply/$', views.apply, name='apply'),

    # /health
    url(r'^health/$', views.health, name='health'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
