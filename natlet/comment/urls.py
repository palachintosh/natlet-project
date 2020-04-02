from django.urls import path
from .views import CommentView


urlpatterns = [
    path('post/comment/', CommentView.as_view(), name="comment_action_url"),
]