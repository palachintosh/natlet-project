from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Photos)
admin.site.register(Tag)