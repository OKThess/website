from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Team, Mentor, Meetup


class ProgramViewTests(TestCase):
    def test_teams(self):
        """
        The program_teams view.
        """
        new_team = Team.objects.create(
            name = 'OK!Thess',
            description = 'The best team.',
            url = 'http://www.okthess.gr/',
            image = SimpleUploadedFile(
                name='mock.jpg',
                content=open('./main/tests/mock.jpg', 'rb').read(),
                content_type='image/jpeg'
            ),
        )
        url = reverse('main:program_teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_team.name)
        self.assertContains(response, new_team.description)
        self.assertContains(response, new_team.url)

    def test_mentors(self):
        """
        The program_mentors view.
        """
        new_mentor = Mentor.objects.create(
            name = 'Bill Gates',
            description = 'Microsoft Founder',
            image = SimpleUploadedFile(
                name='mock.jpg',
                content=open('./main/tests/mock.jpg', 'rb').read(),
                content_type='image/jpeg'
            ),
            github = 'https://github.com/vasilis',
            linkedin = 'https://www.linkedin.com/in/bill',
            website = 'https://billgates.com',
        )
        url = reverse('main:program_mentors')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_mentor.name)
        self.assertContains(response, new_mentor.description)
