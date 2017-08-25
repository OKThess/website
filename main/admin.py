from django.contrib import admin

from .models import Team, Job, Mentor, Meetup, Coworking, Post, Event, Application

admin.site.register(Team)
admin.site.register(Job)
admin.site.register(Mentor)
admin.site.register(Meetup)
admin.site.register(Coworking)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Application)
