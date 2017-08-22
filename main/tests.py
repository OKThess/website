import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Team, Job, Mentor, Meetup, Coworking, Post, Event
from .forms import ApplicationForm


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


class NewsViewTests(TestCase):
    def test_news(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
        )
        url = reverse('main:news')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.slug)
        self.assertContains(response, new_post.teaser)

    def test_news_single(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
        )
        url = reverse('main:news_single', args=[new_post.slug])
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.body)

    def test_featured_news(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
            is_featured = True,
        )
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.teaser)


class EventsViewTests(TestCase):
    def test_events(self):
        new_event = Event.objects.create(
            date = datetime.datetime.now(),
            title = 'Event title',
            link = 'https://www.meetup.com/random-event',
            time_start = datetime.datetime.now(),
            time_end = datetime.datetime.now(),
            organizer = 'OK!Thess',
            organizer_link = 'http://okthess.gr',
            description = 'The most interesting event.',
        )
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_event.title)
        self.assertContains(response, new_event.description)
        self.assertContains(response, new_event.link)


class ApplicationFormTests(TestCase):
    def test_form_valid(self):
        form_data = {
            'answer_1': 'one answer',
            'answer_2': 'two anwers',
            'answer_3': 'three anwers',
            'answer_4': 'four anwers',
            'phonenumber': '2310123456',
            'email': 'tester@okthess.gr',
            'name': 'Tester',
        }
        form = ApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['answer_1'], form_data['answer_1'])
        self.assertEqual(form.cleaned_data['answer_2'], form_data['answer_2'])
        self.assertEqual(form.cleaned_data['answer_3'], form_data['answer_3'])
        self.assertEqual(form.cleaned_data['answer_4'], form_data['answer_4'])
        self.assertEqual(form.cleaned_data['phonenumber'], form_data['phonenumber'])
        self.assertEqual(form.cleaned_data['email'], form_data['email'])
        self.assertEqual(form.cleaned_data['name'], form_data['name'])

    def test_form_invalid_email(self):
        form_data = {
            'answer_1': 'one answer',
            'answer_2': 'two anwers',
            'answer_3': 'three anwers',
            'answer_4': 'four anwers',
            'phonenumber': '2310123456',
            'email': 'okthess.gr',
            'name': 'Tester',
        }
        form = ApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())
