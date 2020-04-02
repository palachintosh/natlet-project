from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control field-width"}),
            'email': forms.TextInput(attrs={"class": "form-control field-width"}),
            'body': forms.Textarea(attrs={"class": "form-control"}),
        }
    
    hidden_slug = forms.CharField(widget=forms.HiddenInput())
    