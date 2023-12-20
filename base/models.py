from django.db import models
# myapp/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name=models.CharField(max_length=30,null=False)
    phone=models.CharField(max_length=10,null=False,blank=True,unique=True)
    
    
class CitizenUser(CustomUser):
    pass
    

class StaffUser(CustomUser):
    position=models.CharField(max_length=10,null=False)
    village_code=models.CharField(max_length=10,null=False,default=None)
    
class CitizenDetails(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=20,null=False)
    house_no=models.IntegerField(null=False)
    house_name=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=20,null=False)
    aadhar_no=models.CharField(max_length=12,null=False)
    ration_no=models.IntegerField()
    account_no=models.IntegerField(null=False)
    ifsc=models.CharField(max_length=11,null=False)
    description=models.TextField(null=False)
    village_code=models.CharField(max_length=10,null=False,default=None)
    survey_result=models.BooleanField(default=False)
    
class Survey(models.Model):
    username=models.ForeignKey(CitizenDetails, on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False)
    house_no=models.IntegerField(null=False)
    house_name=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=20,null=False)
    survey_desc=models.TextField()
    estimated_loss=models.DecimalField(decimal_places=2,max_digits=8)

class Transfer(models.Model):
    user=models.ForeignKey(CitizenUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False)
    phone_no=models.CharField(max_length=10,null=False,blank=True,unique=True)
    account_no=models.IntegerField(null=False)
    ifsc=models.CharField(max_length=11,null=False)
    amount_sent=models.DecimalField(decimal_places=2,max_digits=8,null=False)