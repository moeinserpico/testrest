from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import *
from webapp.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from webapp.forms import *
from datetime import date, timedelta


####################################################################

class util:
    @staticmethod
    def getlastAmar():
        #print("3122");
        company=Amar.objects.filter(timestamp=datetime.date.today())
        return company
    @staticmethod
    def getLastMonth():
        Company=Amar.objects.raw("SELECT avg(fi) as fi , avg(meghdar)as meghdar ,mahsool_id  , avg(fi) * sum(meghdar),id   from amar where pmonth(timestamp)=pmonth(CURRENT_DATE) GROUP by mahsool_id")
        return Company
    @staticmethod
    def getLastWeek():
         Company=Amar.objects.raw("SELECT avg(fi) as fi , avg(meghdar) as meghdar ,mahsool_id , avg(fi) * sum(meghdar),id    from amar where week(timestamp)=week(CURRENT_DATE) GROUP by mahsool_id")
         return Company
    @staticmethod
    def getResult(id):
        if(id=="1"):
            return util.getlastAmar()
        elif(id=="2"):
            return util.getLastWeek()
        else:
            return util.getLastMonth()

def list_amar_rep(request):
    #
    print(datetime.date.today())
    books =util.getlastAmar()

    return render(request, 'webapp/amar_rep/amarList.html', {'amars': books})
def list_amar_rep_type(request,id):
    #    print(datetime.date.today())
    books =util.getResult(id)

    data=dict()
    data['form_is_valid'] = True
    data['html_amar_list'] = render_to_string('webapp/amar_rep/partialAmarlist.html', {
         'amars': books
     })

    return JsonResponse(data)


##########################################################
