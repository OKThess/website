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

    # /teams/
    url(r'^teams/$', views.get_teams, name='teams'),
]
