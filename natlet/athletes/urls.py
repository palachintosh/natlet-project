from .views import AthleteView, Score1, ModalShow
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', AthleteView.as_view(), name="athlete_list_url"),
    #url(r'^ajax/table_show/$', ModalShow.as_view(), name="modal_show_url"),
    path('score_table/', Score1.as_view(), name="score_page_url"),
    path('score_table/show_table/', ModalShow.as_view(), name="show_table"),
]