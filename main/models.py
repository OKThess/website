from datetime import date

from django.db import models
from django.contrib.auth.models import User
from s3direct.fields import S3DirectField


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    description_el = models.TextField()
    url = models.URLField()
    industry = models.CharField(max_length=200)
    image = S3DirectField(dest='uploads')
    alumni = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    description_el = models.TextField()
    image = S3DirectField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, default=None)
    current_title = models.CharField(max_length=100, null=True, default=None)
    current_company = models.CharField(max_length=100, null=True, default=None)
    expertise = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    yearsExp = models.PositiveSmallIntegerField(null=True, default=None)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    website = models.URLField(null=True)

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


class Post(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    teaser = models.TextField()
    teaser_el = models.TextField()
    image = S3DirectField(dest='uploads')
    body = models.TextField()
    body_el = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()

    def __str__(self):
        return self.name
