from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Job(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=100)
    apply_url = models.URLField()

    def __str__(self):
        return self.title


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
