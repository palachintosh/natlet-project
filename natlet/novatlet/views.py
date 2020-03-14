from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from .models import Post, Gallery
from .forms import *

from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.template import RequestContext
from django.db.models import Q
import os.path



# Create your views here.

class Index(View):
    model = Post

    def get(self, request):
        posts = Post.objects.all()

        return render(request, 'novatlet_temp/index.html', context={"posts": posts})


class PostDetail(View):
    model = Post

    def get(self, request, slug):
        get_object = get_object_or_404(self.model, slug__iexact=slug)
        p = get_object.related_gallery
        gallery = Photos.objects.filter(location=p)

        return render(request, 'novatlet_temp/post_detail.html', context={
                        self.model.__name__.lower(): get_object,
                        'gallery': gallery,
                        })


class GallaryCreate(View):
    model = [LocationForm, PhotoForm]

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

class TagList(View):
    model = Tag

    def get(self, request):
        get_tag = Tag.objects.all()
        return render(request, 'novatlet_temp/tag_list.html', context={'get_tag': get_tag})

class TagDetail(View):
    model = Tag
    def get(self, request, slug):
        get_tag = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, 'novatlet_temp/tag_detail.html', context={'tag_detail': get_tag})



# handlers zone

def custom_handler404(request, exception):
    context = RequestContext(request)
    response = render_to_response('404.html', context={'context': context})
    response.status_code = 404
    return response

#Мед в голове

class AthleteView(View):
    model = Athlete
    filter_form = FilterForm

    def get(self, request):
        get_athlete = self.model.objects.all()
        filter_row = self.filter_form

        return render(request, 'novatlet_temp/athlete_list.html', context={
                                                                'get_athlete': get_athlete,
                                                                'filter_row': filter_row
                                                                })
    
    def post(self, request):
        if request.POST:
            bound_form = self.filter_form(request.POST)

            if bound_form.has_changed:
                #get_athlete = self.model.objects.filter(gender=request.POST['gender'])
                
                valid_fields = {}
                get_athlete = []

                for i in bound_form.fields:
                    valid_fields.update({i: request.POST[i]})
                
                def filter_object(valid_value):
                    if valid_value.get('name') == '' and valid_value.get('birthday') == '':
                        if valid_value.get('gender') == 'None':
                            get_filter_object = self.model.objects.all()
                            return get_filter_object
                        get_filter_object = self.model.objects.filter(gender=valid_value.get('gender'))
                    
                    elif valid_value.get('name') != '':
                        get_filter_object = self.model.objects.filter(
                            (Q(name__icontains=valid_value.get('name')) | Q(second_name__icontains=valid_value.get('name'))) | Q(gender=valid_value.get('gender')))

                    elif valid_value.get('birthday') != '':
                        get_filter_object = self.model.objects.filter(Q(birth_year=valid_value.get('birthday')))

                    
                    return get_filter_object

                get_athlete = filter_object(valid_fields)
                print(get_athlete)
                AVALIABLE_CONTENT = get_athlete.count()
    




                return render(request, 'novatlet_temp/athlete_list.html', context={
                                                                                'get_athlete': get_athlete,
                                                                                'av_content': AVALIABLE_CONTENT,
                                                                                'filter_row': self.filter_form,
                                                                                   })

            return redirect(reverse("athlete_list_url"))