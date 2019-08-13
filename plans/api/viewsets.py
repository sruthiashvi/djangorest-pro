from plans.models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans,Preform,Postform,Dongleform,Feedback
from plans.api.serializers import Prepaidserializer,LoginSerializer,InquirySerializer,RechargeSerializer,DongleSerializer,PreformSerializer,PostformSerializer,DongleformSerializer,FeedbackSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
class PrepaidViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Prepaidplans.objects.all()
    serializer_class=Prepaidserializer
class LoginViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Login.objects.all()
    serializer_class=LoginSerializer
class InquiryViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
        queryset=Inquiry.objects.all()
        serializer_class=InquirySerializer
class RechargeViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Recharge.objects.all()
    serializer_class=RechargeSerializer

class DongleViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Dongleplans.objects.all()
    serializer_class=DongleSerializer

class FeedbackViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
class PreformViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Preform.objects.all()
    serializer_class=PreformSerializer

class PostformViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Postform.objects.all()
    serializer_class=PostformSerializer

class DongleformViewSet(viewsets.ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Dongleform.objects.all()
    serializer_class=DongleformSerializer
