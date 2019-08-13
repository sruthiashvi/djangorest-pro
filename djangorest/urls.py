"""djangorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from plans.api.viewsets import PrepaidViewSet,LoginViewSet,InquiryViewSet,RechargeViewSet,DongleViewSet,FeedbackViewSet
#from rest_framework.authtoken.views import obtain_auth_token

router=routers.DefaultRouter()
router.register('plans',PrepaidViewSet) #automaticaly include crud methods
router.register('login',LoginViewSet)
router.register('inquiry',InquiryViewSet)
router.register('recharge',RechargeViewSet)
router.register('dongleplans',DongleViewSet)
router.register('feedback',FeedbackViewSet)

#router.register(r'login',viewsets.LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^",include("plans.urls")),
    path('api/',include(router.urls)), #localhost:8000/api/plans/1/delete 
   # path('auth/',obtain_auth_token)
]
