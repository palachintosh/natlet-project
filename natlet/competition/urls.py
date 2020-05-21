from django.urls import path
from .views import CompetitionView, FutureCompetition

urlpatterns = [
    path('expected_competition', FutureCompetition.as_view(), name="expected_comp_url"),
    path('archive', CompetitionView.as_view(), name="archive_url")
]