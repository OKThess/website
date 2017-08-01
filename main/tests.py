from django.test import TestCase
from django.urls import reverse


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

    def test_teams(self):
        """
        The get_teams view.
        """
        url = reverse('main:teams')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Φιλοξενούμενες ομάδες')
