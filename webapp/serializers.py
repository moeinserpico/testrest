from rest_framework import serializers
from . models import *


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'

class alyaf_kham_va_rangshodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=alyaf_kham_va_rangshode
        fields='__all__'
class alyaf_daraje2_18Serializer(serializers.ModelSerializer):
    class Meta:
        model=alyaf_daraje2_18
        fields='__all__'
class alyaf_jaryan_18Serializer(serializers.ModelSerializer):
    class Meta:
        model=alyaf_jaryan_18
        fields='__all__'
class alyaf_jaryan_30Serializer(serializers.ModelSerializer):
    class Meta:
        model=alyaf_jaryan_30
        fields='__all__'
class alyaf_jaryan_36Serializer(serializers.ModelSerializer):
    class Meta:
        model=alyaf_jaryan_36
        fields='__all__'
class nakh_18Serializer(serializers.ModelSerializer):
    class Meta:
        model=nakh_18
        fields='__all__'

class nakh_2_18Serializer(serializers.ModelSerializer):
    class Meta:
        model=nakh_2_18
        fields='__all__'

class nakh_24Serializer(serializers.ModelSerializer):
    class Meta:
        model=nakh_24
        fields='__all__'

class nakh_30Serializer(serializers.ModelSerializer):
    class Meta:
        model=nakh_30
        fields='__all__'
class nakh_36Serializer(serializers.ModelSerializer):
    class Meta:
        model=nakh_36
        fields='__all__'
class zayeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=zayeat
        fields='__all__'
class bestankariSerializer(serializers.ModelSerializer):
     class Meta:
         model=bestankari
         fields='__all__'
class bedehkariSerializer(serializers.ModelSerializer):
    class Meta:
        model=bedehkari
        fields='__all__'
