from rest_framework import serializers
from plans.models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
class Prepaidserializer(serializers.ModelSerializer):
    class Meta:
        model=Prepaidplans
        fields=('id','planname','planprice','planduration','plandes')
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('id','username','phone','email','password')
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
         model=Inquiry
         fields=('id','name','phone','email','message')
class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
         model=Recharge
         fields=('id','mobile','amount','rdate','pid')

class DongleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongleplans
        fields=('id','planname','data','validity','price')
