from rest_framework import serializers
from .models import Prepaidplans, Dongleplans,Preform,Postform,Dongleform,Pretopostform,Mnpform

class Prepaidserializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    planname=serializers.CharField(max_length=200)
    planprice=serializers.IntegerField()
    planduration=serializers.IntegerField()
    plandes=serializers.CharField(max_length=200)

    
    def create(self,validated_data):
        return Prepaidplans.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.planname=validated_data.get("planname",instance.planname)
        instance.planprice=validated_data.get("planprice",instance.planprice)
        instance.planduration=validated_data.get("planduration",instance.planduration)
        instance.plandes=validated_data.get("plandes",instance.plandes)
        instance.save()
        return instance
class DongleSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    planname=serializers.CharField(max_length=100)
    data=serializers.CharField(max_length=10)
    validity=serializers.CharField(max_length=10)
    price=serializers.CharField(max_length=10)

class PreformSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    mobile=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=10)
    pincode=serializers.CharField(max_length=6)

class PostformSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    mobile=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=10)
    pincode=serializers.CharField(max_length=6)

class DongleformSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    mobile=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=10)
    pincode=serializers.CharField(max_length=6)

class PretopostformSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    mobile=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=10)
    pincode=serializers.CharField(max_length=6)
    newmob=serializers.CharField(max_length=10)

class MnpformSerializer(serializers.Serializer): #convert to json format
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    mobile=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=10)
    pincode=serializers.CharField(max_length=6)
    newmob=serializers.CharField(max_length=10)
