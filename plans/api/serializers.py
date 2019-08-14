from rest_framework import serializers
from plans.models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans,Preform,Postform,Dongleform,Feedback,Pretopostform,Mnpform
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
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=('id','fname','femail','fsubject','fmessage')


class PreformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Preform
        fields=('id','name','email','mobile','address','city','pincode','num')

class PostformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postform
        fields=('id','name','email','mobile','address','city','pincode','num')

class DongleformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongleform
        fields=('id','name','email','mobile','address','city','pincode')
class PretopostformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pretopostform
        fields=('id','name','email','mobile','address','city','pincode','newmob')

class MnpformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mnpform
        fields=('id','name','email','mobile','address','city','pincode','newmob')
