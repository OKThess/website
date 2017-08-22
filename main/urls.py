from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = 'main'
admin.site.site_header = 'OK!Thess administration'
urlpatterns = [
    # /health
    url(r'^health/$', views.health, name='health'),

    # /
    url(r'^$', views.get_index, name='index'),

    # /about/
    url(r'^about/$', views.get_about, name='about'),

    # /teams/
    url(r'^teams/$', views.get_teams, name='teams'),

    # /news/
    url(r'^news/$', views.get_news, name='news'),

    # eg. /news/the-first-blog-post
    url(r'^news/(?P<post_slug>[^/]*)', views.get_news_single, name='news_single'),

    # /apply/
    url(r'^apply/$', views.apply, name='apply'),

    # /contact/
    url(r'^contact/$', views.contact, name='contact'),
]
