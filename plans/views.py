from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import Prepaidplans
from .serializers import Prepaidserializer


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content=JSONRenderer().render(data) #convert python to json
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
@csrf_exempt    
def plans_list(request):
    if request.method=='GET':
        plans=Prepaidplans.objects.all()
        plansserializer=Prepaidserializer(plans,many=True)
        return JSONResponse(plansserializer.data)
    elif request.method=='POST':
        plandata=JSONParser().parse(request)
        plansserializer=Prepaidserializer(data=plandata)
        if plansserializer.is_valid():
            plansserializer.save()
            return JSONResponse(plansserializer.data,
            status=status.HTTP_201_CREATED)
        return JSONResponse(plansserializer.errors,
            status=status.HHTP_400_BAD_REQUEST)
@csrf_exempt
def plans_details(request,pk):
    try:
        plan=Prepaidplans.objects.get(pk=pk)
    except Prepaidplans.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        plansserializer=Prepaidserializer(plan)
        return JSONResponse(plansserializer.data)
    elif request.method=="PUT":
        plandata=JSONParser().parse(request)
        plansserializer=Prepaidserializer(plan,data=plandata)
        if plansserializer.is_valid():
            plansserializer.save()
            return JSONResponse(plansserializer.data)
        return JSONResponse(plansserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        plan.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)