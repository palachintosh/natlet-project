from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, reverse
from .models import Post
from .forms import CommentForm
from django.conf import settings
from django.shortcuts import resolve_url
from urllib.parse import urlencode

import requests

# Create your views here.

class CommentView(View):
    model_form = CommentForm

    def post(self, request):
        bound_form = self.model_form(request.POST)

        base_url = reverse("post_page_url", kwargs={'slug': request.POST['hidden_slug']})
        
        
        if bound_form.is_valid():
            ### captcha validator ###
            recaptcha_response = request.POST['g-recaptcha-response']
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ### captcha validator ###
            

            if result['success']:
                print('success! ')
                add_comment = bound_form.save(commit=False)
                add_comment.comment_for_post = Post.objects.get(slug__iexact=request.POST['hidden_slug'])

                bound_form.save()

                alert_show = False
                query_string = urlencode({'alert_mess': alert_show})
                url = '{}?{}'.format(base_url, query_string)
                
                return redirect(url)

        
        alert_show = True
        query_string = urlencode({'alert_mess': alert_show})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)