from django.db import models
from django.shortcuts import reverse

# Create your models here.


class AthletesScore(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название таблицы")
    score_table = models.TextField(verbose_name="Таблица рекрдов")
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to="scores/", verbose_name="Заставка", default="default.jpg")
    last_update = models.DateField(verbose_name="Последнее обновление", auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absulute_url(self):
        return self.slug