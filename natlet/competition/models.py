from django.db import models
from django.shortcuts import reverse
from natlet.custom_project_utils import gen_slug
import datetime

# Create your models here.


class CompetitionList(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True)
    comp_type = models.CharField(max_length=80, verbose_name='Вид соревнований')
    description = models.TextField(max_length=500, verbose_name='Описание', default='Описание отсутствует')
    rank = models.PositiveIntegerField()
    rank_code = models.CharField(max_length=4, verbose_name='Код страны')
    location = models.CharField(max_length=300, verbose_name='Место проведения')
    comp_date_start = models.DateField(verbose_name='Начало соревнований')
    comp_date_end = models.DateField(verbose_name='Конец соревнований')
    sponsor = models.CharField(max_length=200, verbose_name='Организатор')
    participants = models.CharField(max_length=300, verbose_name='Участники')

    def __str__(self):
        return '{}, {}'.format(self.title, self.comp_date_start)
    
    def get_absolute_url(self):
        pass
        #return reverse('comp_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        print(args, kwargs)
        self.slug = gen_slug(self.title)
        super(CompetitionList, self).save(*args, **kwargs)
