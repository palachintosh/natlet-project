from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from novatlet.models import Athlete
from athletes.models import AthletesScore
from athletes.forms import TestForm
from django.http import HttpResponse

# Create your views here.

class GetReqUrl(View):
    model_form = TestForm

    def get(self, request):

        test_form = self.model_form
        return render(request, 'ajax/ajax.html', locals())


class ModalShow(View):
    model = AthletesScore

    def get(self, request):

        if request.method == 'GET':
            return HttpResponse('success')
        else:
            return HttpResponse("unsuccesful")
        
          
            # <!-- <script src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script> -->

        # name = request.GET.get('username', None)

        # print(name, "-------------------")

        # a = "{% include 'athletes/includes/score_table_modal.html' %}"
        # table = self.model.objects.get(slug__iexact=name)

        # print("---------------name-----------: ", name, table)
        # data = {
        #     'table': table.score_table,
        #     'include_modal': a,
        # }

        # return JsonResponse(data, status="200")
