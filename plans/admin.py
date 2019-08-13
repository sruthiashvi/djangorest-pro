from django.contrib import admin
from .models import Prepaidplans,Login,Inquiry,Recharge,Dongleplans,Preform,Postform,Dongleform,Feedback
# Register your models here.
admin.site.register(Prepaidplans)
admin.site.register(Dongleplans)
admin.site.register(Login)
admin.site.register(Inquiry)
admin.site.register(Recharge)
admin.site.register(Feedback)
admin.site.register(Preform)
admin.site.register(Postform)
admin.site.register(Dongleform)
