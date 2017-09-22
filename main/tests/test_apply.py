from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate

from ..forms import ApplicationForm


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

    def test_apply(self):
        form_data = {
            'answer_1': 'one answer',
            'answer_2': 'two anwers',
            'answer_3': 'three anwers',
            'answer_4': 'four anwers',
            'phonenumber': '2310123456',
            'email': 'tester@okthess.gr',
            'name': 'Tester',
        }
        activate('en')
        url = reverse('main:apply')
        response = self.client.post(url, form_data, follow=True)
        self.assertContains(response, 'Thank you for applying!')
