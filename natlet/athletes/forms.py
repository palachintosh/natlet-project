from django import forms


class FilterForm(forms.Form):
    SELECT_GENDER = [
        ('None', 'Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = forms.ChoiceField(choices=SELECT_GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={
                                                        'class': 'form-control mb-2 mr-sm-2',
                                                        'placeholder': 'Имя или фамилия'
                                                        }), required=False)
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control mb-2 mr-sm-2',
        
        'type': 'date',
    }), required=False)


    def clean_name_and_surname(self):
        ret_name = self.cleaned_data['name'].lower()
        if ret_name == '' or ret_name == None:
            return None
        return ret_name

    def clean_birthday(self):
        print("validate")
        ret_birthday = self.cleaned_data['birthday']
        if ret_birthday == '':
            return None
        return ret_birthday