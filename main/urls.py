from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

from . import views


def health(request):
    return HttpResponse('Ok')


app_name = 'mainapp'
admin.site.site_header = 'OK!Thess administration'
urlpatterns = [
    # /health
    url(r'^health/$', health, name='health'),
]
