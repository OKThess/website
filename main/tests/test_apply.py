from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate
from faker import Faker

from ..forms import ApplicationForm


class ApplicationFormTests(TestCase):
    def test_form_valid(self):
        fake = Faker()
        form_data = {
            'answer_idea_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_3': 'idea',
            'answer_market_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_4': fake.sentence(nb_words=3, ext_word_list=None),
            'name': fake.name(),
            'phonenumber': fake.phone_number(),
            'email': fake.email(),
        }
        form = ApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['answer_idea_1'], form_data['answer_idea_1'])
        self.assertEqual(form.cleaned_data['answer_idea_2'], form_data['answer_idea_2'])
        self.assertEqual(form.cleaned_data['answer_idea_3'], form_data['answer_idea_3'])
        self.assertEqual(form.cleaned_data['answer_market_1'], form_data['answer_market_1'])
        self.assertEqual(form.cleaned_data['answer_market_2'], form_data['answer_market_2'])
        self.assertEqual(form.cleaned_data['answer_market_3'], form_data['answer_market_3'])
        self.assertEqual(form.cleaned_data['answer_team_1'], form_data['answer_team_1'])
        self.assertEqual(form.cleaned_data['answer_team_2'], form_data['answer_team_2'])
        self.assertEqual(form.cleaned_data['answer_support_1'], form_data['answer_support_1'])
        self.assertEqual(form.cleaned_data['answer_support_2'], form_data['answer_support_2'])
        self.assertEqual(form.cleaned_data['answer_support_3'], form_data['answer_support_3'])
        self.assertEqual(form.cleaned_data['answer_support_4'], form_data['answer_support_4'])
        self.assertEqual(form.cleaned_data['phonenumber'], form_data['phonenumber'])
        self.assertEqual(form.cleaned_data['email'], form_data['email'])
        self.assertEqual(form.cleaned_data['name'], form_data['name'])


    def test_form_invalid_email(self):
        fake = Faker()
        form_data = {
            'answer_idea_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_3': 'idea',
            'answer_market_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_4': fake.sentence(nb_words=3, ext_word_list=None),
            'name': fake.name(),
            'phonenumber': fake.phone_number(),
            'email': 'im an invalid email',
        }
        form = ApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_apply(self):
        fake = Faker()
        form_data = {
            'answer_idea_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_idea_3': 'idea',
            'answer_market_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_market_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_team_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_1': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_2': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_3': fake.sentence(nb_words=3, ext_word_list=None),
            'answer_support_4': fake.sentence(nb_words=3, ext_word_list=None),
            'name': fake.name(),
            'phonenumber': fake.phone_number(),
            'email': fake.email(),
        }
        activate('en')
        url = reverse('main:apply')
        response = self.client.post(url, form_data, follow=True)
        self.assertEquals(response.status_code, 200)
        # self.assertContains(response, 'Your application has been submitted. Thank you!')
