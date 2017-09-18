from django.test import TestCase
from django.urls import reverse


class IndexViewsTest(TestCase):
    def test_index(self):
        """
        The index view.
        """
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')

    def test_about(self):
        """
        The about view.
        """
        url = reverse('main:about')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, 'Τι κάνουμε')

    def test_contact(self):
        """
        The contact view.
        """
        url = reverse('main:contact')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
