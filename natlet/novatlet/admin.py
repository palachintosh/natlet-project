from django.contrib import admin
from django import forms
from .models import *
from competition.models import CompetitionList

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

# Register your models here.

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


#admin.site.register(Post, PostAdmin)
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Photos)
admin.site.register(Tag)
admin.site.register(Award)
admin.site.register(Athlete)
admin.site.register(CompetitionList)


