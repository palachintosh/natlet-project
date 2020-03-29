from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.utils.safestring import mark_safe
from django.utils import timezone
from .models import *

import time


class PaginatorObjectMixin:
    #object_mix = None

    def paginator_custom(self, request, posts):
        
        paginator = Paginator(posts, 8)
        pages = request.GET.get('page')
        pag_range = paginator.page_range

        pag_range_len = len(pag_range)

        try:
            count_posts = paginator.page(pages)
        except PageNotAnInteger:
            count_posts = paginator.page(1)
        
        paginator_finished = {'pag_range_len': pag_range_len, 'count_posts': count_posts, 'pag_range': pag_range}

        return paginator_finished
        

        


class DisplayObjectMixin():
    model = None
    template = None

    def get(self, request):
        if self.model.__name__ == 'Tag':
            tags = Tag.objects.all()
            return render(request, self.template, locals())

        object_mix = self.model.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
        p = PaginatorObjectMixin()
        pag_object_mix = p.paginator_custom(request, object_mix)
        admin_obj = True

        return render(request, self.template, context={
                                                      self.model.__name__.lower() + 's': pag_object_mix['count_posts'],
                                                      'paginator_dict': pag_object_mix,
                                                      'admin_obj': admin_obj,
                                                      #'count_posts': p.paginator_custom(request, object_mix)
                                                      })

