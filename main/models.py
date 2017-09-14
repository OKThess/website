from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='main/static/main/uploads/', default='main/static/main/logo.png')

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Meetup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


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
    image = models.ImageField(upload_to='main/static/main/uploads/', default='main/static/main/logo.png')
    body = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    link = models.URLField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    organizer = models.CharField(max_length=200)
    organizer_link = models.URLField()
    description = models.TextField(blank=True)

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
