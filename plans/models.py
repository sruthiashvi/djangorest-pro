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
class Login(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Inquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.name
