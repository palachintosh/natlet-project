from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200, label='Тема', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'width: 40%',
               'placeholder': 'Наприклад: питання вiдносно проведенних змагань',
               'style': 'width: 60%',
            }
    ))

    email = forms.EmailField(max_length=100, label='Ваш e-mail', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'width: 40%',
    }))

    message = forms.CharField(max_length=1000, min_length=80, 
                              widget=forms.Textarea(attrs={
                                                          'class': 'form-control',
                                                          'rows': '6',
                                                        }))
    

    def clean_message(self):
        get_clean_message = self.cleaned_data['message']
        # format_message = 'From: ' + self.cleaned_data['email'] + '\n' + get_clean_message

        return get_clean_message
    
