from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Post
from .forms import CommentForm

# Create your views here.

class CommentView(View):
    model_form = CommentForm
    def post(self, request):
        bound_form = self.model_form(request.POST)

        print("-------------referer is -------------", request.POST['hidden_slug'])


        if bound_form.is_valid():
            add_comment = bound_form.save(commit=False)
            add_comment.comment_for_post = Post.objects.get(slug__iexact=request.POST['hidden_slug'])

            bound_form.save()

        return redirect("index_page_url")