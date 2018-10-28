from django import forms
import datetime
from . models import *
from django.conf import settings
import logging
from django.forms import ModelForm, inlineformset_factory
import jdatetime
from webapp.business.business import *
class AmarForm(forms.ModelForm):

     class Meta:
        model = Amar
        fields = '__all__'

class BedehForm(forms.ModelForm):

     class Meta:
        model = Bedehkar
        fields = '__all__'

class HazineForm(forms.ModelForm):
     def clean_timestamp(self):
         cleaned_data = super(HazineForm, self).clean()
         value=self.cleaned_data['timestamp']

         value=Utils.getDate(value);
         return value
     class Meta:
        model = Hazine
        fields = '__all__'

class TalabForm(forms.ModelForm):

     class Meta:
        model = Talab
        fields = '__all__'
