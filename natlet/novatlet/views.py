# from django.shortcuts import render
# from django.shortcuts import redirect
from django.shortcuts import render_to_response
from .models import Post, Gallery
from comment.models import Comment
from .forms import *
from .utils import *
from comment.views import CommentView
from comment.forms import CommentForm
from natlet.custom_project_utils import GetRandomSidebarPost

from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


import os.path



# Create your views here.

class Variables:
    def post_filter_utils(self):
        post_filter = Post.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
        return post_filter

class Index(DisplayObjectMixin, View):
    model = Post
    template = 'novatlet_temp/index.html'



class CustomSearch(DisplayObjectMixin, View):
    model = Post
    template = 'novatlet_temp/index.html'



class PostDetail(View, GetRandomSidebarPost):
    model = Post
    model_form = CommentForm
   
    def get(self, request, slug):
        alert_show = request.GET.get('alert_mess')

        get_object = get_object_or_404(self.model, slug__iexact=slug)
        p = get_object.related_gallery
        gallery = Photos.objects.filter(location=p)
        admin_obj = True

        comment = Comment.objects.filter(comment_for_post=get_object)
        comment_form = self.model_form(data={'hidden_slug': slug})

        get_sidebar_posts = GetRandomSidebarPost(model=self.model).get_newest_post()

        return render(request, 'novatlet_temp/post_detail.html', context={
                        self.model.__name__.lower(): get_object,
                        'gallery': gallery,
                        'admin_obj': admin_obj,
                        'comment': comment,
                        'comment_form': comment_form,
                        'returned_slug': slug,
                        'get_sidebar_posts': get_sidebar_posts,
                        })

class TagList(LoginRequiredMixin, DisplayObjectMixin, View):
    model = Tag
    template = 'novatlet_temp/tag_list.html'
    raise_exception = True


class TagDetail(View):
    def get(self, request, slug):
        get_tag = get_object_or_404(Tag, slug__iexact=slug)
        admin_obj = True

        return render(request, 'novatlet_temp/tag_detail.html', context={'tag_detail': get_tag, 'admin_obj': admin_obj})



class GallaryCreate(LoginRequiredMixin, View):
    model = [LocationForm, PhotoForm]
    raise_exception = True

    def get(self, request):
        gallery_form = self.model[0]
        gallery_form_0 = self.model[1]

        location_field = gallery_form_0.GetPhotoField()

        return render(request, 'novatlet_temp/gallery_create.html', context={
                        'gallery': gallery_form,
                        'gallery_0': gallery_form_0,
                        'location_field': location_field, 
                        })

                        
    def post(self, request):
        if request.POST:
            bound_form_0 = self.model[0](request.POST) #LocationForm: dir_object
            bound_form_1 = self.model[1](request.POST, request.FILES) #PhotoForm: location, img_object 
        
            if bound_form_0.is_valid() or bound_form_1.is_valid():
                def save_after_validate(self, request, directory_object):
                    
                    for f in request.FILES.getlist('img_object'):
                        data = f.read()
                        photo = Photos(location = Location.objects.order_by('id').last()) # it works
                        photo.img_object.save(save_path(directory_object) + str(f.name), ContentFile(data))
                        photo.save()
                        print("success 2 !", photo)

                def save_path(directory_object):
                    save_path = directory_object + "/photos/"
                    return save_path
            

                if not bound_form_0.cleaned_data.get('boolean'):
                    print("we are here")
                    if request.POST['dir_object'] == '':
                        return render(request, 'novatlet_temp/gallery_create.html', context={
                                                'gallery': bound_form_0,
                                                'gallery_0': bound_form_1,
                                                'location_field': bound_form_1.GetPhotoField(), 
                                                    })
                    bound_form_0.save()
                    directory_object = request.POST['dir_object']

                    save_after_validate(self, request, directory_object)


                if bound_form_0.cleaned_data.get('boolean'):
                    if request.POST['dir_object'] != '':
                        return render(request, 'novatlet_temp/gallery_create.html', context={
                                                'gallery': bound_form_0,
                                                'gallery_0': bound_form_1,
                                                'location_field': bound_form_1.GetPhotoField(), 
                                                    })
                    directory_object = Location.objects.get(id=request.POST['location']).__str__()
                    
                    save_after_validate(self, request, directory_object)
                 
            return render(request, 'novatlet_temp/gallery_create.html', context={
                                       'gallery': bound_form_0,
                                       'gallery_0': bound_form_1,
                                       'location_field': bound_form_1.GetPhotoField(), 
                                         })


# handlers zone

def custom_handler404(request, exception):
    context = RequestContext(request)
    response = render_to_response('404.html', context={'context': context})
    response.status_code = 404
    return response

#Мед в голове

