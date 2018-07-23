from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from s3direct.fields import S3DirectField
from ckeditor.fields import RichTextField


class EnTeamManager(models.Manager):
    def get_queryset(self):
        return super(EnTeamManager, self).get_queryset().exclude(description_en=u'').exclude(description_en=None)


class ElTeamManager(models.Manager):
    def get_queryset(self):
        return super(ElTeamManager, self).get_queryset().exclude(description_el=u'').exclude(description_el=None)


class Team(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    description_en = models.TextField(null=True, default=None)
    description_el = models.TextField(null=True, default=None)
    url = models.URLField(null=True, blank=True, default=None)
    industry = models.CharField(max_length=200)
    image = S3DirectField(dest='uploads')
    alumni = models.BooleanField(default=False)

    objects = models.Manager()
    el_objects = ElTeamManager()
    en_objects = EnTeamManager()

    def __str__(self):
        if self.name:
            return self.name
        elif self.url:
            return self.url
        else:
            return '* Team'


class EnMentorManager(models.Manager):
    def get_queryset(self):
        return super(EnMentorManager, self).get_queryset().exclude(description_en=u'').exclude(description_en=None)


class ElMentorManager(models.Manager):
    def get_queryset(self):
        return super(ElMentorManager, self).get_queryset().exclude(description_el=u'').exclude(description_el=None)


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    description_en = models.TextField(null=True, default=None)
    description_el = models.TextField(null=True, default=None)
    image = S3DirectField(dest='uploads')
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, default=None)
    current_title = models.CharField(max_length=100, null=True, default=None)
    current_company = models.CharField(max_length=100, null=True, default=None)
    expertise = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    yearsExp = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    objects = models.Manager()
    el_objects = ElMentorManager()
    en_objects = EnMentorManager()

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    description_en = models.TextField(null=True, blank=True, default=None)
    description_el = models.TextField(null=True, blank=True, default=None)
    title = models.CharField(max_length=300, null=True, blank=True)
    image = S3DirectField(dest='uploads')

    def __str__(self):
        return self.name


class Meetup(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    link = models.URLField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    date_end = models.DateField(null=True, blank=True, default=None)
    organizer = models.CharField(max_length=200)
    organizer_link = models.URLField()
    description = models.TextField(blank=True)
    image = S3DirectField(dest='uploads')
    meetup = models.ForeignKey(
        Meetup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @property
    def is_old(self):
        return date.today() > self.date

    def __str__(self):
        return self.title


class Coworking(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class EnPostManager(models.Manager):
    def get_queryset(self):
        return super(EnPostManager, self).get_queryset() \
            .exclude(title_en=u'') \
            .exclude(title_en=None) \
            .exclude(teaser_en=u'') \
            .exclude(teaser_en=None) \
            .exclude(body_en=u'') \
            .exclude(body_en=None)


class ElPostManager(models.Manager):
    def get_queryset(self):
        return super(ElPostManager, self).get_queryset() \
            .exclude(title_el=u'') \
            .exclude(title_el=None) \
            .exclude(teaser_el=u'') \
            .exclude(teaser_el=None) \
            .exclude(body_el=u'') \
            .exclude(body_el=None)


class Post(models.Model):
    date = models.DateField()
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_el = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    teaser_en = models.TextField(null=True, blank=True)
    teaser_el = models.TextField(null=True, blank=True)
    image = S3DirectField(dest='uploads')
    body_en = RichTextField(null=True, blank=True)
    body_el = RichTextField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    objects = models.Manager()
    el_objects = ElPostManager()
    en_objects = EnPostManager()

    def __str__(self):
        if not self.title_en and not self.title_el:
            return date.strftime('%x')
        else:
            if self.title_en:
                return self.title_en
            else:
                return self.title_el
        return 'no_title'


class ImageMedia(models.Model):
    image = S3DirectField(dest='uploads')

    def __str__(self):
        return self.image


class Application(models.Model):
    date_applied = models.DateField(default=timezone.now, null=True, blank=True)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    answer_idea_1 = models.TextField(default='default')
    answer_idea_2 = models.TextField(default='default')

    IDEA = 'idea'
    PROTOTYPE = 'prototype'
    USERS = 'users'
    REVENUE = 'revenue'
    STAGE_CHOICES = (
        (IDEA, 'Idea'),
        (PROTOTYPE, 'Prototype'),
        (USERS, 'Early users'),
        (REVENUE, 'Early revenue'),
    )
    answer_idea_3 = models.CharField(
        choices=STAGE_CHOICES,
        max_length=50,
        default=IDEA,
    )

    answer_market_1 = models.TextField(default='default')
    answer_market_2 = models.TextField(default='default')
    answer_market_3 = models.TextField(default='default')
    answer_team_1 = models.TextField(default='default')
    answer_team_2 = models.TextField(default='default')
    answer_support_1 = models.TextField(default='default')
    answer_support_2 = models.TextField(default='default')
    answer_support_3 = models.TextField(default='default')
    answer_support_4 = models.TextField(default='default')

    def __str__(self):
        return self.name


class About(models.Model):
    what_text_en = RichTextField(null=True, blank=True)
    what_text_el = RichTextField(null=True, blank=True)
    how_text_en = RichTextField(null=True, blank=True)
    how_text_el = RichTextField(null=True, blank=True)
    participate_text_en = RichTextField(null=True, blank=True)
    participate_text_el = RichTextField(null=True, blank=True)
    coworking_text_en = RichTextField(null=True, blank=True)
    coworking_text_el = RichTextField(null=True, blank=True)

    def __str__(self):
        return 'About page'


class OkthessMeetup(models.Model):
    date = models.DateField()
    time = models.TimeField()
    title = models.TextField(null=True, blank=True)
    agenda = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class ResourceCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    is_pinned = models.BooleanField(default=False)
    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class ApplyText(models.Model):
    content_en = RichTextField(null=True, blank=True)
    content_el = RichTextField(null=True, blank=True)

class WeekendApplication(models.Model):
    weekend_date_applied = models.DateField(default=timezone.now, null=True, blank=True)
    first_name= models.TextField()
    last_name= models.TextField()
    email= models.EmailField()
    specialization= models.TextField()
    accept_terms= models.BooleanField(default=False)
