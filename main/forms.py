from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'answer_idea_1',
            'answer_idea_2',
            'answer_idea_3',
            'answer_market_1',
            'answer_market_2',
            'answer_market_3',
            'answer_team_1',
            'answer_team_2',
            'answer_support_1',
            'answer_support_2',
            'answer_support_3',
            'answer_support_4',
            'phonenumber',
            'email',
            'name',
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    message = forms.CharField(max_length=20000)
    email = forms.EmailField()
