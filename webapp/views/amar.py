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
from datetime import datetime,date
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from webapp.forms import *

from django.contrib.auth.decorators import login_required
####################################################################

class util:
    @staticmethod
    def getlastAmar():
        company=Amar.objects.filter(timestamp=date.today())
        return company

@login_required
def list_amar(request,id=None):
    #    print(datetime.date.today())

    books =util.getlastAmar()
    return render(request, 'webapp/amar/amarList.html', {'amars': books})
##########################################################


@login_required
def list_lastday_amar(request):
    data=dict()
    books=util.getlastAmar()
    data['html_amar_list'] = render_to_string('webapp/amar/partialAmarList.html', {               'amars': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)

@login_required
def list_lastweek_amar(request):
    data=dict()
    books=Utils.getListAmarLastWeek()
    data['html_amar_list'] = render_to_string('webapp/amar/partialAmarList.html', {               'amars': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)

@login_required
def list_lastmonth_amar(request):
    data=dict()
    books=Utils.getListAmarLastMonth()
    data['html_amar_list'] = render_to_string('webapp/amar/partialAmarList.html', {               'amars': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)


##########################################################

##########################################################

def save_amar_form(request, form, template_name):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = util.getlastAmar()
            data['html_amar_list'] = render_to_string('webapp/amar/partialAmarList.html', {
                'amars': books
            })
        else:
            print(form.errors)
            data['form_is_valid'] = False

    context = {'form': form}


    data['html_amar_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def amar_delete(request, id):
    comp1 = get_object_or_404(Amar, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        companies =  util.getlastAmar()
        #Tasks.objects.filter(amarId=id).update(amar=id)
        data['html_amar_list'] = render_to_string('webapp/amar/partialAmarList.html', {'amars': companies })
    else:
        context = {'amar': comp1}
        data['html_amar_form'] = render_to_string('webapp/amar/partialAmarDelete.html',context,request=request,)
    return JsonResponse(data)

##########################################################

##########################################################
def amar_create(request):
    if (request.method == 'POST'):
        form = AmarForm(request.POST)
        return save_amar_form(request, form, 'webapp/amar/partialAmarCreate.html')
    else:

        form = AmarForm()
        return save_amar_form(request, form, 'webapp/amar/partialAmarCreate.html')




##########################################################
def amar_update(request, id):
    company= get_object_or_404(Amar, id=id)
    template=""
    if (request.method == 'POST'):
        form = AmarForm(request.POST, instance=company)
    else:
        form = AmarForm(instance=company)


    return save_amar_form(request, form,"webapp/amar/partialAmarUpdate.html")
##########################################################

##########################################################
