from django.shortcuts import render
from django.views import View
from .models import CompetitionList
import datetime


# Create your views here.


class CompetitionView(View):
    model = CompetitionList

    def get(self, request):
        get_competition = self.model.objects.filter(comp_date_start__lt=datetime.datetime.today())
        return render(request, 'competition/competition.html', locals())


class FutureCompetition(View):
    model = CompetitionList
    
    def get(self, request):
        get_competition = self.model.objects.filter(comp_date_start__gte=datetime.datetime.today())
        return render(request, 'competition/future_competition.html', locals())