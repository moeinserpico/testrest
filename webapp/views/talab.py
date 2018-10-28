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
    def getlastTalab():
        company=Talab.objects.filter(timestamp=datetime.date.today())
        return company

def list_talab(request,id=None):
    #
    print(datetime.date.today())
    books =util.getlastTalab()

    return render(request, 'webapp/talab/talabList.html', {'talabs': books})


##########################################################

def save_talab_form(request, form, template_name):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = util.getlastTalab()
            data['html_talab_list'] = render_to_string('webapp/talab/partialTalabList.html', {                'talabs': books            })
        else:
            print(form.errors)
            data['form_is_valid'] = False

    context = {'form': form}


    data['html_talab_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def talab_delete(request, id):
    comp1 = get_object_or_404(Talab, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        companies =  util.getlastTalab()
        #Tasks.objects.filter(talabId=id).update(talab=id)
        data['html_talab_list'] = render_to_string('webapp/talab/partialTalabList.html', {            'talabs': companies        })
    else:
        context = {'talab': comp1}
        data['html_talab_form'] = render_to_string('webapp/talab/partialTalabDelete.html',            context,            request=request,        )
    return JsonResponse(data)

##########################################################

##########################################################
def talab_create(request):
    if (request.method == 'POST'):
        form = TalabForm(request.POST)
        return save_talab_form(request, form, 'webapp/talab/partialTalabCreate.html')
    else:

        form = TalabForm()
        return save_talab_form(request, form, 'webapp/talab/partialTalabCreate.html')




##########################################################
def talab_update(request, id):
    company= get_object_or_404(Talab, id=id)
    template=""
    if (request.method == 'POST'):
        form = TalabForm(request.POST, instance=company)
    else:
        form = TalabForm(instance=company)


    return save_talab_form(request, form,"webapp/talab/partialTalabUpdate.html")
##########################################################

##########################################################
