from django.contrib import admin
from django import forms
from .models import *
from comment.models import Comment
from competition.models import CompetitionList
from athletes.models import AthletesScore

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



class CommentAdminForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm

class AthletesScoreAdminForm(forms.ModelForm):
    score_table = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AthletesScore
        fields = '__all__'

@admin.register(AthletesScore)
class AthletesScoreAdmin(admin.ModelAdmin):
    form = AthletesScoreAdminForm




#admin.site.register(Post, PostAdmin)
#admin.site.register(AthletesScore)
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Photos)
admin.site.register(Tag)
admin.site.register(Award)
admin.site.register(Athlete)
admin.site.register(CompetitionList)

#admin.site.register(Comment, CommentAdmin)

