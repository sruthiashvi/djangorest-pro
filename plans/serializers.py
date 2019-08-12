from rest_framework import serializers
from .models import Prepaidplans, Dongleplans

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