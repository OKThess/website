from django.test import TestCase
from django.urls import reverse

from .models import Team, Job, Mentor, Meetup, Coworking


class GetViewsTest(TestCase):
    def test_index(self):
        """
        The get_index view.
        """
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Συνεργάτης')
        self.assertContains(response, 'στα πρώτα βήματα')

    def test_about(self):
        """
        The get_about view.
        """
        url = reverse('main:about')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Σχετικά')


class TeamsViewTests(TestCase):
    def test_teams(self):
        """
        The get_teams view.
        """
        new_team = Team.objects.create(
            name = 'OK!Thess',
            description = 'The best team.',
            url = 'http://www.okthess.gr/',
            image_url = 'http://www.okthess.gr/logo.png',
        )
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
        self.assertContains(response, new_team.name)
        self.assertContains(response, new_team.description)
        self.assertContains(response, new_team.url)

    def test_jobs(self):
        """
        The get_teams view.
        """
        new_team = Team.objects.create(
            name = 'OK!Thess',
            description = 'The best team.',
            url = 'http://www.okthess.gr/',
            image_url = 'http://www.okthess.gr/logo.png',
        )
        new_job = Job.objects.create(
            team = new_team,
            title = 'Web Developer',
            apply_url = 'http://www.okthess.gr/jobs',
        )
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
        self.assertContains(response, new_job.title)
        self.assertContains(response, new_job.apply_url)

    def test_mentors(self):
        """
        The get_teams view.
        """
        new_mentor = Mentor.objects.create(
            name = 'Mentor name',
            description = 'The best mentor',
        )
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
        self.assertContains(response, new_mentor.name)
        self.assertContains(response, new_mentor.description)

    def test_meetups(self):
        """
        The get_teams view.
        """
        new_meetup = Meetup.objects.create(
            name = 'Node.js meetup',
            description = 'The best meetup',
        )
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
        self.assertContains(response, new_meetup.name)
        self.assertContains(response, new_meetup.description)

    def test_coworkings(self):
        """
        The get_teams view.
        """
        new_coworking = Coworking.objects.create(
            name = 'Coho',
            description = 'The best coworking',
        )
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
        self.assertContains(response, new_coworking.name)
        self.assertContains(response, new_coworking.description)
