from plans.models import Prepaidplans,Login
from plans.api.serializers import Prepaidserializer,LoginSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
class PrepaidViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Prepaidplans.objects.all()
    serializer_class=Prepaidserializer
class LoginViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Login.objects.all()
    serializer_class=LoginSerializer