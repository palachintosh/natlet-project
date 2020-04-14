from django.shortcuts import render, reverse
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import View
from django.http import JsonResponse

from novatlet.models import Athlete
from .models import AthletesScore
from .forms import FilterForm, TestForm


# Create your views here.


class AthleteView(View):
    model = Athlete
    filter_form = FilterForm

    def get(self, request):
        get_athlete = self.model.objects.all()
        filter_row = self.filter_form

        return render(request, 'athletes/athlete_list.html', context={
                                                                'get_athlete': get_athlete,
                                                                'filter_row': filter_row
                                                                })
    
    def post(self, request):
        if request.POST:
            bound_form = self.filter_form(request.POST)

            if bound_form.has_changed:

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

                return render(request, 'athletes/athlete_list.html', context={
                                                                                'get_athlete': get_athlete,
                                                                                'av_content': AVALIABLE_CONTENT,
                                                                                'filter_row': self.filter_form,
                                                                                   })

            return redirect(reverse("athlete_list_url"))


class Score(View):
    model = AthletesScore
    model_form = TestForm
    def get(self, request):
        best_score = self.model.objects.all()
        girls = best_score.get(slug="girls")
        juniors = best_score.get(slug="juniors")

        test_form = self.model_form

        return render(request, 'athletes/score_table.html', locals())

    def post(self, request):
        pass

class ModalShow(View):
    model = AthletesScore

    def get(self, request):
        print('--------------ajax---------------')
        print('--------------ajax---------------')

        name = request.GET.get('username', None)

        print(name, "-------------------")

        a = "{% include 'athletes/includes/score_table_modal.html' %}"
        table = self.model.objects.get(slug__iexact=name)

        print("---------------name-----------: ", name, table)
        data = {
            'table': table.score_table,
            'include_modal': a,
        }

        return JsonResponse(data)