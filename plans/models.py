from django.db import models

# Create your models here.
class Prepaidplans(models.Model):
    planname=models.CharField(max_length=100)
    planprice=models.FloatField()
    planduration=models.IntegerField()
    plandes=models.TextField()
    
    class Meta:
        ordering=("planprice",) #-planprice for reverse order #tuple so ,
    def __str__(self):
        return self.planname #display names in the admin panel