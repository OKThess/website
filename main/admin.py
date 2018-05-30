from django.contrib import admin

from .models import Team, Mentor, Meetup, Coworking, Post, Event, Application, \
    ImageMedia, About, OkthessMeetup, ResourceCategory, Resource, ApplyText, Partner

admin.site.register(Team)
admin.site.register(Mentor)
admin.site.register(Meetup)
admin.site.register(Coworking)
admin.site.register(Event)
admin.site.register(ImageMedia)
admin.site.register(About)
admin.site.register(OkthessMeetup)
admin.site.register(ResourceCategory)
admin.site.register(Resource)
admin.site.register(ApplyText)

# Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_el', 'title_en', 'slug', 'is_featured')

admin.site.register(Post, PostAdmin)

# Application
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'answer_idea_3')

admin.site.register(Application, ApplicationAdmin)

# Partner
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(Partner, PartnerAdmin)
