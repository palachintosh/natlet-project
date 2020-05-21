from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.utils.safestring import mark_safe
from django.utils import timezone
from .models import *
from natlet import settings
from natlet.custom_project_utils import GetRandomSidebarPost
from django.db.models import Q

import requests
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
        
        paginator_finished = {
                              'pag_range_len': pag_range_len,
                              'count_posts': count_posts,
                              'pag_range': pag_range,
                              }

        return paginator_finished
        



class DisplayObjectMixin:
    
    def __init__(self, alert_mess=None):
        self.alert_mess = True
    

    model = None
    template = None

    def get(self, request):
        if self.model.__name__ == 'Tag':
            tags = Tag.objects.all()
            return render(request, self.template, locals())
        
        search_q = request.GET.get('search', '')
        object_mix = self.model.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
        
        if search_q:
            object_mix = self.model.objects.filter(Q(title__icontains=search_q) | Q(body__icontains=search_q))
            self.alert_mess = False

        p = PaginatorObjectMixin()
        pag_object_mix = p.paginator_custom(request, object_mix)
        admin_obj = True

        get_sidebar_post = GetRandomSidebarPost(model=Post)
        f = get_sidebar_post.get_newest_post()

        return render(request, self.template, context={
                                                      self.model.__name__.lower() + 's': pag_object_mix['count_posts'],
                                                      'paginator_dict': pag_object_mix,
                                                      'admin_obj': admin_obj,
                                                      #'count_posts': p.paginator_custom(request, object_mix)
                                                      'get_sidebar_post': f,
                                                      'alert_mess': self.alert_mess,
                                                      })



class CaptchaChecking:
    
    def capcha_response(self, request):
        recaptcha_response = request.POST['g-recaptcha-response']
        data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        
        return result