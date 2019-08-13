from django.contrib import admin
from .models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans,Feedback

# Register your models here.
admin.site.register(Prepaidplans)
admin.site.register(Dongleplans)
admin.site.register(Login)
admin.site.register(Inquiry)
admin.site.register(Recharge)
admin.site.register(Feedback)