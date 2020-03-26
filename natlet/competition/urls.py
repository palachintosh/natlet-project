from django.urls import path
from .views import CompetitionView

urlpatterns = [
    path('archive', CompetitionView.as_view(), name="archive_url")
]