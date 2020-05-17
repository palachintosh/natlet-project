from .views import ModalShow, GetReqUrl
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', GetReqUrl.as_view(), name="list"),
    path('like/', ModalShow.as_view(), name="like"),
]