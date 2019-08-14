from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Prepaidplans,Login,Dongleplans,Preform,Postform,Dongleform,Pretopostform,Mnpform
from plans.api.serializers import Prepaidserializer,LoginSerializer,DongleSerializer,PreformSerializer,PostformSerializer,DongleformSerializer,PretopostformSerializer,MnpformSerializer
from django.conf.urls import url,include
from .serializers import DongleSerializer


# Create your views here.
class DongleViewSet(viewsets.ModelViewSet):
   
    queryset = Dongleplans.objects.all()
    serializer_class = DongleSerializer