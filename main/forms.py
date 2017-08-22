from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'phonenumber', 'email', 'name']
        widgets = {
            'answer_1': forms.Textarea(attrs={
                'cols': 50,
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Ποιά είναι η επιχειρηματική ιδέα που θέλετε να αναπτύξετε στο OK!Thess (Έως 150 λέξεις);',
            }),
            'answer_2': forms.Textarea(attrs={
                'cols': 50,
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Σε ποιά αγορά απευθύνεσθε (πού βλέπετε τους μελλοντικούς πελάτες) (έως 100 λέξεις);',
            }),
            'answer_3': forms.Textarea(attrs={
                'cols': 50,
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Γνωρίζετε ποιος είναι ο ανταγωνισμός στην ιδέα σας (έως 100 λέξεις);',
            }),
            'answer_4': forms.Textarea(attrs={
                'cols': 50,
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Τι περιμένετε να σας προσφέρει το OK!Thess εκτός από χώρο και υποδομή (έως 100 λέξεις);',
            }),
            'phonenumber': forms.TextInput(attrs={'placeholder': 'Τηλέφωνο επικοινωνίας', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ονοματεπώνυμο', 'class': 'form-control'}),
        }
