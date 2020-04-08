from django.db import models
from novatlet.models import Post

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=180, verbose_name="Ваше iм'я: ")
    email = models.EmailField()
    body = models.CharField(max_length=700, db_index=True, verbose_name="Коментар: ")
    time = models.DateTimeField(auto_now_add=True)
    comment_for_post = models.ForeignKey(Post, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email