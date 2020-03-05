from django.db import models
from django.shortcuts import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.

class Location(models.Model):
    dir_object = models.CharField(max_length=100, default='', blank=True, db_index=True, unique=True)
    #boolean = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.dir_object


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    description = models.TextField(max_length=400, db_index=True)
    body = models.TextField(db_index=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post_img = models.ImageField(upload_to='images/', null=True)

    related_gallery = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_page_url', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title



class Gallery(models.Model):
    title = title = models.CharField(max_length=200, db_index=True)
    img_object = models.ImageField(upload_to='images/test/', null=True)

    related_gallery = models.ForeignKey(Post, models.SET_NULL, blank=True, null=True)


#photos/

# def save_path(*args, **kwargs):
#     with open("/home/lesha/Python/athletic_project/natlet/novatlet/config.cfg") as f:
#         for i in f:
#             sp = i
#     sp + str(args[1])
#     return sp

    # save_path_var = Location.objects.order_by('id').last()
    # if save_path_var != '':
    #     return str(save_path_var.dir_object + '/')
    # return "default/"
    

class Photos(models.Model):
    #img_object = models.ImageField(upload_to=save_path(), db_index=True, verbose_name="Images")
    img_object = models.ImageField(upload_to='gallery/', db_index=True, verbose_name="Images")
    # location = models.ForeignKey(Location, models.CASCADE, related_name='photos')
    location = models.ForeignKey('Location', models.CASCADE, related_name='photos', blank=True, null=True)


# @receiver(pre_save, sender=Photos)
# def add_save_path(instance, *args, **kwargs):
#     related_path = instance.img_object
#     # related_path.save()
#     #related_path.upload_to = save_path(args, kwargs)
#     print(instance)
    

    
    #related_path.save()
