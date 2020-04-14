from .views import AthleteView, Score, ModalShow
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', AthleteView.as_view(), name="athlete_list_url"),
   # url(r'^ajax/table_show/$', ModalShow.as_view(), name="modal_show_url"),
    path('score_table/ajax/table_show/', ModalShow.as_view(), name="modal_show_url"),
    path('score_table/', Score.as_view(), name="score_page_url"),
]