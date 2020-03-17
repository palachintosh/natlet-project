from django import forms
from django.forms import formset_factory
from .models import *
from django.core.exceptions import ValidationError
import os.path

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['dir_object']

        widgets = {
            'dir_object': forms.TextInput(attrs={"class": "form-control"}),
        }
    boolean = forms.BooleanField(required=False, label='Gallery already exist: ')

    def clean_dir_object(self):
        cleaned_form_field = self.cleaned_data['dir_object'].lower()

        # if cleaned_form_field == '':
        #     raise ValidationError('Fill the "New location field" or choose exist location!')
        return cleaned_form_field


    # def clean(self):
    #     cleaned_data = super(LocationForm, self).clean()
    #     cleaned_dir_field = self.cleaned_data['dir_object'].lower()
    #     boolean =  self.cleaned_data['boolean']
    #     print(boolean)
    #     if cleaned_dir_field != '' and boolean:
    #         raise ValidationError("Choose exist directory OR input the new path")
    #     if cleaned_dir_field == '' and not boolean:
    #         raise ValidationError("'New_directoy' can't be empty")
    #     return cleaned_dir_field



class PhotoForm(forms.Form):
    class GetPhotoField(forms.ModelForm):
        class Meta:
            model = Photos
            fields = ['location']

            widgets = {
                'location': forms.Select(attrs={'class': 'form-control'}),
            }

        def clean_location(self):
            print("cleaned_data")
            cleaned_form_field = self.cleaned_data['location']
            if cleaned_form_field == None or cleaned_form_field == '':
                return cleaned_form_field
            return cleaned_form_field

    img_object = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


    # def save(self):
    #     new_add_dir = Photos.objects.create(
    #         img_object = self.cleaned_data['img_object']
    #     )
    #     return new_add_dir



        



# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photos
#         fields = ['img_object', 'location']

#         widgets = {
#             'img_object': forms.FileInput(attrs={'multiple': True,
#                                                 'class': 'form-control',
#                                                 # 'enctype': 'multipart/form-data',
#                                                 }),
#             'location': forms.SelectMultiple(attrs={'class': 'form-control'}),
#         }

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
