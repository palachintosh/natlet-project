from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index_page_url"),
    path('search/', CustomSearch.as_view(), name="search_func_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_page_url"),
    path('tag/', TagList.as_view(), name="tag_list_url"),
    path('tag/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
    path('gallery-create/upload/', GallaryCreate.as_view(), name="gallery_create_url"),
    #path('hale_of_fame/athletes/', AthleteView.as_view(), name="athlete_list_url"),
    #path('competition/archive/', ArchivePage.as_view(), name="archive_url"),
    #path('contacts/', Contacts.as_view(), name="contact_page_url"),
]