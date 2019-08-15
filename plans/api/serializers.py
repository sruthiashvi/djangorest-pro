from rest_framework import serializers
from plans.models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans,Preform,Postform,Dongleform,Feedback,Pretopostform,Mnpform
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email','first_name','last_name') 
        extra_kwargs={'password':{'write_only':True,'required':True}} 
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user 
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
         fields=('id','name','phone','email','message','postedby')
class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
         model=Recharge
         fields=('id','mobile','amount','rdate','pid','postedby')

class DongleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongleplans
        fields=('id','planname','data','validity','price')
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=('id','fname','femail','fsubject','fmessage','postedby')


class PreformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Preform
        fields=('id','name','email','mobile','address','city','pincode','num','postedby')

class PostformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postform
        fields=('id','name','email','mobile','address','city','pincode','num','postedby')

class DongleformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongleform
        fields=('id','name','email','mobile','address','city','pincode','postedby')
class PretopostformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pretopostform
        fields=('id','name','email','mobile','address','city','pincode','newmob','postedby')

class MnpformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mnpform
        fields=('id','name','email','mobile','address','city','pincode','newmob','postedby')
