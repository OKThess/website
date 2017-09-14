import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Team, Mentor, Meetup, Coworking, Post, Event
from .forms import ApplicationForm


class GetViewsTest(TestCase):
    def test_index(self):
        """
        The get_index view.
        """
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
