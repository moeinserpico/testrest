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
from django.contrib.auth.decorators import login_required
####################################################################

class util:
    @staticmethod
    def getlastBedeh():
        company=Bedehkar.objects.filter(timestamp=datetime.date.today())
        return company
@login_required
def list_bedeh(request,id=None):
    #
    print(datetime.date.today())
    books =util.getlastBedeh()

    return render(request, 'webapp/bedeh/bedehList.html', {'bedehs': books})


##########################################################

def save_bedeh_form(request, form, template_name):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = util.getlastBedeh()
            data['html_bedeh_list'] = render_to_string('webapp/bedeh/partialBedehList.html', {                'bedehs': books            })
        else:
            print(form.errors)
            data['form_is_valid'] = False

    context = {'form': form}


    data['html_bedeh_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def bedeh_delete(request, id):
    comp1 = get_object_or_404(Bedehkar, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        companies =  util.getlastBedeh()
        #Tasks.objects.filter(bedehId=id).update(bedeh=id)
        data['html_bedeh_list'] = render_to_string('webapp/bedeh/partialBedehList.html', {            'bedehs': companies        })
    else:
        context = {'bedeh': comp1}
        data['html_bedeh_form'] = render_to_string('webapp/bedeh/partialBedehDelete.html',     context,            request=request,        )
    return JsonResponse(data)

##########################################################

##########################################################
def bedeh_create(request):
    if (request.method == 'POST'):
        form = BedehForm(request.POST)
        return save_bedeh_form(request, form, 'webapp/bedeh/partialBedehCreate.html')
    else:

        form = BedehForm()
        return save_bedeh_form(request, form, 'webapp/bedeh/partialBedehCreate.html')




##########################################################
def bedeh_update(request, id):
    company= get_object_or_404(Bedehkar, id=id)
    template=""
    if (request.method == 'POST'):
        form = BedehForm(request.POST, instance=company)
    else:
        form = BedehForm(instance=company)


    return save_bedeh_form(request, form,"webapp/bedeh/partialBedehUpdate.html")
##########################################################

##########################################################
