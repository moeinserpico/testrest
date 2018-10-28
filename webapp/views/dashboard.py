from django.shortcuts import get_object_or_404,redirect
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
import jdatetime
from webapp.forms import *
from datetime import date, timedelta
from webapp.business.business import Utils
from django.contrib.auth.decorators import login_required
import json
from webapp.views import *
@login_required
def index(request):

            return redirect(list_dashboard)

@login_required
def list_dashboard(request):

    if (request.user.is_authenticated):
        if(request.user.username == "admin"):
               return render(request,"webapp/dashboard/main.html")
        else:
               return redirect(list_amar)

def getMojudiAlyaf(request):
    data=dict()
    n1=Utils.getSumMojudiAlyaf()

    data['html_mojudi_alyaf_list'] = render_to_string('webapp/dashboard/partialAlyaf.html', {
                 'x1': format(n1,",.0f")


             })
    data['html_is_valid']=True

    return JsonResponse(data)


def getTalab(request):
    data=dict()
    n1=Utils.getSumTalabByDate()


    data['html_talab_list'] = render_to_string('webapp/dashboard/partialTalab.html', {
                 'x1': format(n1,",.0f")


             })
    data['html_is_valid']=True

    return JsonResponse(data)
def getBedeh(request):
    data=dict()
    n1=Utils.getSumBedehByDate()


    data['html_bedeh_list'] = render_to_string('webapp/dashboard/partialBedeh.html', {
                 'x1': format(n1,",.0f")


             })
    data['html_is_valid']=True

    return JsonResponse(data)
def getHazine(request):
    data=dict()
    n1=Utils.getSumHazineByDate()
    print("seda mizane to ro")


    data['html_hazine_list'] = render_to_string('webapp/dashboard/partialHazine.html', {
                 'x1': format(n1,",.0f")


             })
    data['html_is_valid']=True

    return JsonResponse(data)
def getLineChart(request):
    data=dict()
    n1=Utils.get_N_Bedehkar()
    n2=Utils.get_N_Bestankar()
    data1=[]
    data2=[]

    for x in n1:
         record={'month':x.month,'val':x.id}

         data1.append(record)
    for x in n2:
         record={'month':x.month,'val':x.id}
         data2.append(record)
    return JsonResponse({'n1':data1,'n2':data2})

#############################Mahsool Bar Chart#####################
def getBarChart(request):

    n1=Utils.get_N_Mahsool()

    data1=[]


    for x in n1:
         record={'month':x.month,'val':x.id}

         data1.append(record)

    return HttpResponse(json.dumps(data1), content_type='application/json')

###################################Mahsoo Pie chart##############
def getMahsoolPie(request):
    c1=Utils.getCurrentNakh()
    c2=Utils.getCurrentAlyaf()
    c3=Utils.getCurrentZayeat()
    return JsonResponse({'nakh':c1,'alyaf':c2,'zayeat':c3})

############################# Hazine Bar Chart #####################
def getHazineLineChart(request):

    n1=Utils.get_N_Hazine()

    data1=[]


    for x in n1:
         record={'month':x.month,'val':x.id}

         data1.append(record)

    return HttpResponse(json.dumps(data1), content_type='application/json')

##################### Get Total #####################################
def getTotal(request):
    data=dict()
    c1=Utils.getSumAmarByDate()
    c2=Utils.getSumBedehByDate()
    c3=Utils.getSumTalabByDate()
    c4=Utils.getSumHazineByDate()
    c5=c1-c2-c3-c4
    data['html_total_list'] = render_to_string('webapp/dashboard/partialOveral.html', {'x1': format(c5,",.0f")})
    data['html_is_valid']=True

    return JsonResponse(data)
