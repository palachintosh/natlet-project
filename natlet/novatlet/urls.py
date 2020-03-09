from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index_page_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_page_url"),
    path('tag/', TagList.as_view(), name="tag_list_url"),
    path('tag/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
    path('gallery-create/upload/', GallaryCreate.as_view(), name="gallery_create_url"),
]