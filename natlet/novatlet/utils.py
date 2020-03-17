from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.utils.safestring import mark_safe
from .models import *
import time

class DisplayObjectMixin:
    model = None
    template = None

    def get(self, request):
        object_mix = self.model.objects.all()

        return render(request, self.template, context={self.model.__name__.lower() + 's': object_mix})