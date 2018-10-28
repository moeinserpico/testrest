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
from webapp.business import *
# Create your views here.
@api_view(['GET', 'POST'])
def employee_list(request):
   if request.method == 'GET':
        emp=employee.objects.all()
        ser=employeeSerializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=employeeSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)

@api_view(['GET', 'POST'])
def alyaf_kham_va_rangshode_list(request):
   if request.method == 'GET':
        emp=alyaf_kham_va_rangshode.objects.order_by('-id')[:1]
        ser=alyaf_kham_va_rangshodeSerializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=alyaf_kham_va_rangshodeSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET'])
def alyaf_kham_va_rangshode_date(request,date):
   dt=datetime.datetime.strptime(date, "%Y-%m-%d")
   print(dt)
   if request.method == 'GET':
        emp=alyaf_kham_va_rangshode.objects.filter(timestamp=dt)
        ser=alyaf_kham_va_rangshodeSerializer(emp,many=True)
        return Response(ser.data)


@api_view(['GET', 'POST'])
def alyaf_daraje2_18_list(request):
   if request.method == 'GET':
        emp=alyaf_daraje2_18.objects.all().order_by('-id')[:1]
        ser=alyaf_daraje2_18Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=alyaf_daraje2_18Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)

@api_view(['GET', 'POST'])
def alyaf_jaryan_18_list(request):
   if request.method == 'GET':
        emp=alyaf_jaryan_18.objects.all().order_by('-id')[0]
        ser=alyaf_jaryan_18Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=alyaf_jaryan_18Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def alyaf_jaryan_30_list(request):
   if request.method == 'GET':
        emp=alyaf_jaryan_30.objects.all().order_by('-id')[0]
        ser=alyaf_jaryan_30Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=alyaf_jaryan_30Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def alyaf_jaryan_36_list(request):
   if request.method == 'GET':
        emp=alyaf_jaryan_36.objects.all().order_by('-id')[0]
        ser=alyaf_jaryan_36Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=alyaf_jaryan_36Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def nakh_18_list(request):
   if request.method == 'GET':
        emp=nakh_18.objects.all().order_by('-id')[0]
        ser=nakh_18Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=nakh_18Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def nakh_2_18_list(request):
   if request.method == 'GET':
        emp=nakh_2_18.objects.all().order_by('-id')[0]
        ser=nakh_2_18Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=nakh_2_18Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def nakh_24_list(request):
   if request.method == 'GET':
        emp=nakh_24.objects.all().order_by('-id')[0]
        ser=nakh_24Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=nakh_24Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def nakh_30_list(request):
   if request.method == 'GET':
        emp=nakh_30.objects.all().order_by('-id')[0]
        ser=nakh_30Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=nakh_30Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def nakh_36_list(request):
   if request.method == 'GET':
        emp=nakh_36.objects.all().order_by('-id')[0]
        ser=nakh_36Serializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=nakh_36Serializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def zayeat_list(request):
   if request.method == 'GET':
        emp=zayeat.objects.all().order_by('-id')[0]
        ser=zayeatSerializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=zayeatSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def bestankari_list(request):
   if request.method == 'GET':
        emp=abestankari.objects.all().order_by('-id')[0]
        ser=bestankariSerializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=bestankariSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
@api_view(['GET', 'POST'])
def bedehkari_list(request):
   if request.method == 'GET':
        emp=bedehkari.objects.all().order_by('-id')[0]
        ser=bedehkariSerializer(emp,many=True)
        return Response(ser.data)
   elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser=bedehkariSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return JsonResponse(ser.data,status=201)
        JsonResponse(ser.errors,status=400)
