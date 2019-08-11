from rest_framework import serializers
from plans.models import Prepaidplans,Login,Inquiry
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
class Prepaidserializer(serializers.ModelSerializer):
    class Meta:
        model=Prepaidplans
        fields=('id','planname','planprice','planduration','plandes')
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('id','name','phone','email','password')
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
         model=Inquiry
         fields=('id','name','phone','email','message')