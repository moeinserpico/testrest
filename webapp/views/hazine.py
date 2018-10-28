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
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from webapp.forms import *
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from webapp.business.business import Utils
####################################################################

class util:
    @staticmethod
    def getlastHazine():
        company=Hazine.objects.filter(timestamp=date.today())
        return company
@login_required
def list_hazine(request,id=None):
    # print(datetime.date.today())
    books =util.getlastHazine()

    return render(request, 'webapp/hazine/hazineList.html', {'hazines': books})


@login_required
def list_lastday_hazine(request):
    data=dict()
    books=util.getlastHazine()
    data['html_hazine_list'] = render_to_string('webapp/hazine/partialHazineList.html', {               'hazines': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)

@login_required
def list_lastweek_hazine(request):
    data=dict()
    books=Utils.getListHazineLastWeek()
    data['html_hazine_list'] = render_to_string('webapp/hazine/partialHazineList.html', {               'hazines': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)

@login_required
def list_lastmonth_hazine(request):
    data=dict()
    books=Utils.getListHazineLastMonth()
    data['html_hazine_list'] = render_to_string('webapp/hazine/partialHazineList.html', {               'hazines': books            })
    data['form_is_valid'] = True
    return JsonResponse(data)


##########################################################

def save_hazine_form(request, form, template_name):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = util.getlastHazine()
            #books=Hazine.objects.all()
            data['html_hazine_list'] = render_to_string('webapp/hazine/partialHazineList.html', {               'hazines': books            })
        else:
            print(form.errors)
            data['form_is_valid'] = False

    context = {'form': form}


    data['html_hazine_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def hazine_delete(request, id):
    comp1 = get_object_or_404(Hazine, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        companies =  util.getlastHazine()
        #Tasks.objects.filter(hazineId=id).update(hazine=id)
        data['html_hazine_list'] = render_to_string('webapp/hazine/partialHazineList.html', {            'hazines': companies        })
    else:
        context = {'hazine': comp1}
        data['html_hazine_form'] = render_to_string('webapp/hazine/partialHazineDelete.html',            context,            request=request,        )
    return JsonResponse(data)

##########################################################

##########################################################
def hazine_create(request):
    if (request.method == 'POST'):
        form = HazineForm(request.POST)
        return save_hazine_form(request, form, 'webapp/hazine/partialHazineCreate.html')
    else:
        dt=Utils.getTitleDate()

        form = HazineForm()#initial={'timestamp':dt}
        return save_hazine_form(request, form, 'webapp/hazine/partialHazineCreate.html')




##########################################################
def hazine_update(request, id):
    company= get_object_or_404(Hazine, id=id)
    template=""
    if (request.method == 'POST'):
        form = HazineForm(request.POST, instance=company)
    else:
        form = HazineForm(instance=company)


    return save_hazine_form(request, form,"webapp/hazine/partialHazineUpdate.html")
##########################################################

##########################################################
