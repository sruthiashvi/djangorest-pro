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
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Inquiry(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    postedby=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Recharge(models.Model):
    mobile=models.CharField(max_length=10) 
    amount=models.CharField(max_length=10)  
    rdate=models.CharField(max_length=50)
    pid=models.CharField(max_length=10)
    postedby=models.CharField(max_length=15)
    def __str__(self):
        return self.mobile

class Dongleplans(models.Model):
    planname=models.CharField(max_length=100)
    data=models.CharField(max_length=10)
    validity=models.CharField(max_length=10)
    price=models.CharField(max_length=10)

    class Meta:
        ordering=('price',)
        verbose_name='Dongleplan'
    
    def __str__(self):
        return self.planname #display names in the admin panel
class Feedback(models.Model):
    fname=models.CharField(max_length=100)
    femail=models.CharField(max_length=100)
    fsubject=models.CharField(max_length=100)
    fmessage=models.CharField(max_length=1000)
    postedby=models.CharField(max_length=15)



class Preform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    num=models.CharField(max_length=10)
    postedby=models.CharField(max_length=15)

    class Meta:
        ordering=('name',)
        verbose_name='Preform'
    
    def __str__(self):
        return self.name

class Postform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    num=models.CharField(max_length=10)
    postedby=models.CharField(max_length=15)
    class Meta:
        ordering=('name',)
        verbose_name='Postform'
    
    def __str__(self):
        return self.name

class Dongleform(models.Model):
    name=models.CharField(max_length=110)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    postedby=models.CharField(max_length=15)

    class Meta:
        ordering=('name',)
        verbose_name='Dongleform'
    
    def __str__(self):
        return self.name

class Pretopostform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    newmob=models.CharField(max_length=10)
    postedby=models.CharField(max_length=15)

    class Meta:
        ordering=('name',)
        verbose_name='Pretopostform'
    
    def __str__(self):
        return self.name

class Mnpform(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    newmob=models.CharField(max_length=10)
    postedby=models.CharField(max_length=10)

    class Meta:
        ordering=('name',)
        verbose_name='Mnpform'
    
    def __str__(self):
        return self.name