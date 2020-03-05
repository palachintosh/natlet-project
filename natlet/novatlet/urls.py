from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index_page_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_page_url"),
    path('gallery-create/upload/', GallaryCreate.as_view(), name="gallery_create_url"),
]