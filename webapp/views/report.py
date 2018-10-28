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
import jdatetime
from webapp.forms import *
from datetime import date, timedelta
from webapp.business.business import Utils
from django.contrib.auth.decorators import login_required
@login_required
def getReport(request,dt=None):
    dtTitle=Utils.getTitleDate(dt)
    amars=Utils.getAmarReportByDate(dt)
    bedehs=Utils.getBedehReportByDate(dt)
    talabs=Utils.getTalabReportByDate(dt)
    hazines=Utils.getHazineReportByDate(dt)
    sumAmar=Utils.getSumAmarByDate(dt)
    sumTalab=Utils.getSumTalabByDate(dt)
    sumBedeh=Utils.getSumBedehByDate(dt)
    sumHazine=Utils.getSumHazineByDate(dt)
    sumDashte=format((sumAmar+sumTalab),",.0f")
    sumNadashte=format((sumBedeh+sumHazine),",.0f")
    total=format((sumAmar+sumTalab-sumBedeh-sumHazine),",.0f")
    #format(sum,",.0f")

    return render(request, 'webapp/report/repList.html', {'amars': amars,'bedehs':bedehs,'talabs':talabs,'dtTitle':dtTitle,'hazines':hazines,'total':total,'sumTalab':sumDashte,'sumBedeh':sumNadashte})
