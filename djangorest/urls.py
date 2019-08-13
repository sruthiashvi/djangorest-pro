from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from plans.api.viewsets import PrepaidViewSet,LoginViewSet,InquiryViewSet,RechargeViewSet,DongleViewSet,PreformViewSet,PostformViewSet,DongleformViewSet,FeedbackViewSet
#from rest_framework.authtoken.views import obtain_auth_token

router=routers.DefaultRouter()
router.register('plans',PrepaidViewSet) #automaticaly include crud methods
router.register('login',LoginViewSet)
router.register('inquiry',InquiryViewSet)
router.register('recharge',RechargeViewSet)
router.register('dongleplans',DongleViewSet)
router.register('feedback',FeedbackViewSet)
router.register('form1',PreformViewSet)
router.register('form2',PostformViewSet)
router.register('form3',DongleformViewSet)

#router.register(r'login',viewsets.LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^",include("plans.urls")),
    path('api/',include(router.urls)), #localhost:8000/api/plans/1/delete 
   # path('auth/',obtain_auth_token)
]
