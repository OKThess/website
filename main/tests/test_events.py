import datetime

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Event, Meetup


class EventsViewTests(TestCase):
    def test_meetups(self):
        """
        The events view, test sidebar meetups.
        """
        new_meetup = Meetup.objects.create(
            name = 'Node.js meetup',
            description = 'The best meetup',
            link = 'https://meetup.com/SKGNode',
        )
        url = reverse('main:events')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_meetup.name)
        self.assertContains(response, new_meetup.link)

    def test_events(self):
        """
        The events view.
        """
        new_event = Event.objects.create(
            date = datetime.datetime.now(),
            title = 'Event title',
            link = 'https://www.meetup.com/random-event',
            time_start = datetime.datetime.now(),
            time_end = datetime.datetime.now(),
            organizer = 'OK!Thess',
            organizer_link = 'http://okthess.gr',
            description = 'The most interesting event.',
            image = SimpleUploadedFile(
                name='mock.jpg',
                content=open('./main/tests/mock.jpg', 'rb').read(),
                content_type='image/jpeg'
            ),
        )
        url = reverse('main:events')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_event.title)
        self.assertContains(response, new_event.description)
        self.assertContains(response, new_event.link)
