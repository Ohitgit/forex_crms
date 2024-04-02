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
    gender = models.CharField(max_length = 50,null=True,db_index=True)
    state=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    country=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    live_account_limit=models.IntegerField(null=True,blank=True,db_index=True)
    demo_account_limit=models.IntegerField(null=True,blank=True,db_index=True)
    address=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    user_wallet=models.FloatField(null=True,blank=True,db_index=True)
    def __str__(self):
        return self.username

class LiveAccount(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,db_index=True)
    ip=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    login=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    email=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    group=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    group_name=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    leverage=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    main_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    invest_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    phone_password=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    country=models.CharField(null=True,blank=True,db_index=True,max_length=100)









class UploadDocument(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_index=True)
    documenttype=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    identitytype=models.CharField(null=True,blank=True,db_index=True,max_length=100)
    img=models.FileField(null=True,db_index=True,upload_to='img/')
    img2=models.FileField(null=True,db_index=True,upload_to='img2/')
    datetime=models.DateTimeField(null=True,default=timezone.now)

    



class UserDeposits(BaseModel):
   
  

    wallet_choice = (
        ("wallet", 'Wallet'),
        ("live", 'Live'),
      
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True,
        blank = True,
        db_index = True)
    currency = models.TextField(null=True,blank=True,db_index=True)
    client_id= models.BigIntegerField(default=0, null=True, blank=True,db_index=True)
    transaction_ID = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    recipet = models.FileField(upload_to='user_upload_document',null=True, blank=True,db_index=True)
    ip_address = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    amount = models.FloatField(default=0)
    added_on = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_on = models.DateTimeField(auto_now=True,db_index=True)
    action_choice = models.CharField(default=0, choices=wallet_choice,db_index=True )
    deposit_from = models.TextField(null=True, blank=True,db_index=True)
    comment = models.TextField(null=True, blank=True,db_index=True)
    reject = models.TextField(null=True, blank=True,db_index=True)
    status=models.BooleanField(default=False,db_index=True)
    def __str__(self):
        return '{0}'.format(self.user)
    

class Internal_Transfer(BaseModel):
    transfer_from = models.TextField(null=True,blank=True,db_index=True)
    transfer_to = models.TextField(null=True,blank=True,db_index=True)
    amount= models.TextField(null=True,blank=True,db_index=True)
    transaction_id = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    ip_address = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    datetime=models.DateTimeField(null=True,default=timezone.now)
    def __str__(self):
        return '{0}'.format(self.transaction_id)