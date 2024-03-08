from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class BaseModel(models.Model):
    added_on = models.DateTimeField(default=timezone.now,db_index=True)
    updated_on = models.DateTimeField(auto_now=True,db_index=True)
    class Meta:
        abstract = True


class Otp_Status(BaseModel):
    otp_status=models.BooleanField(default=False)
class Client_Register(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_index=True)
    first_name=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    last_name=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    email=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    email_status=models.BooleanField(default=False)
    mobile_no=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    dob=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    mobile_status=models.BooleanField(default=False)
    username=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    uuid=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    password=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    pincode=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    city=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    state=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    country=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    live_account_limit=models.IntegerField(null=True,blank=True,db_index=True)
    demo_account_limit=models.IntegerField(null=True,blank=True,db_index=True)
    gender=models.CharField(null=True,blank=True,db_index=True,max_length=200)


    def __str__(self):
        return self.username

class LiveAccount(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_index=True)
    ip=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    login=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    email=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    group=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    leverage=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    main_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    invest_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    phone_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    country=models.CharField(null=True,blank=True,db_index=True,max_length=100)
   


