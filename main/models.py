from django.db import models

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
