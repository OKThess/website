from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'phonenumber', 'email', 'name']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    message = forms.CharField(max_length=20000)
    email = forms.EmailField()
