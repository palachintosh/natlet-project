from .views import AthleteView
from django.urls import path

urlpatterns = [
    path('', AthleteView.as_view(), name="athlete_list_url"),
]