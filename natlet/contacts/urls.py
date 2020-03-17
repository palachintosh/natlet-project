from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', Contacts.as_view(), name="contact_p_url"),
]