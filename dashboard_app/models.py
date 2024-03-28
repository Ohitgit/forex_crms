from django.db import models
from django.utils import timezone
# Create your models here.


class BaseModel(models.Model):
    added_on = models.DateTimeField(default=timezone.now,db_index=True)
    updated_on = models.DateTimeField(auto_now=True,db_index=True)
    class Meta:
        abstract = True


class Add_Leverage(BaseModel):
      add_leverage_value=models.IntegerField(null=True,blank=True,db_index=True)
      def __str__(self):
           return str(self.add_leverage_value)


class Add_Currency(BaseModel):
      name=models.CharField(null=True,blank=True,db_index=True,max_length=200)
      def __str__(self):
       return self.name

        
class Forex_Group(BaseModel):
    name=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    def __str__(self):
      return self.name

class Demo_Account(BaseModel):
    amount=models.CharField(null=True,blank=True,db_index=True,max_length=200)
    def __str__(self):
      return self.amount
    
class Create_Forex_Group(BaseModel):
     Account_type = (('live account', 'Live Account'), ('demo account', 'Demo Acount'),)
     account_name= models.CharField( max_length=20,choices=Account_type, default='live account',db_index=True)
     account_feture=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     feture_value=models.CharField(max_length=200,null=True,blank=True,db_index=True)

     def __str__(self) -> str:
           return self.account_name
    


class Company_Profile(BaseModel):
     name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     logo=models.ImageField(null=True,upload_to='company/logo')
     mobile_no=models.CharField(max_length=100,null=True,blank=True,db_index=True)
     facebook_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     linkdin_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     whatsapp_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     telegram_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     instagram_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     twitter_link=models.CharField(max_length=200,null=True,blank=True,db_index=True)

     def __str__(self) -> str:
          return self.name
    

class Email_Setting(BaseModel):
     EMAIL_BACKEND=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     EMAIL_USE_TLS=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     EMAIL_HOST =models.CharField(max_length=200,null=True,blank=True,db_index=True)
     EMAIL_PORT =models.CharField(max_length=200,null=True,blank=True,db_index=True)
     EMAIL_HOST_USER =models.CharField(max_length=200,null=True,blank=True,db_index=True)
     EMAIL_HOST_PASSWORD=models.CharField(max_length=200,null=True,blank=True,db_index=True)

     def __str__(self) -> str:
          return self.EMAIL_PORT
     


class Add_Platform_Link(BaseModel):
       link_type = (('android link', 'Android Link'), ('ios link', 'Ios Link'), ('desktop link', 'Desktop Link'))
       link= models.CharField( max_length=20,choices=link_type, default='live account',db_index=True)

       def __str__(self) -> str:
          return self.link
       
class Forex_Manager_Credential(BaseModel):
     ip=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     login=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     password=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     def __str__(self) -> str:
          return self.ip



class Country(BaseModel):
     shortname=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     code=models.IntegerField(null=True,blank=True,db_index=True)
     def __str__(self) -> str:
          return self.shortname




class Bank_Detail(BaseModel):
    user_type = (('client', 'Client'), ('staff', 'Staff'), ('admin', 'Admin'))
    user_type_name= models.CharField( max_length=20,choices=user_type, default='client',db_index=True)
    benificary_name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
    ifsc_code=models.CharField(max_length=200,null=True,blank=True,db_index=True)
    bank_name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
    account_name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
   
    def __str__(self) -> str:
          return self.benificary_name
    



class Wallet(BaseModel):
    user_type = (('client', 'Client'), ('staff', 'Staff'), ('admin', 'Admin'))
    user_type_name= models.CharField( max_length=20,choices=user_type, default='client',db_index=True)
    wallet_type = (('usdt', 'USDT'), ('btc', 'BTC'), ('eth', 'ETH'))
    wallet_type_name= models.CharField( max_length=20,choices=user_type, default='usdt',db_index=True)
    wallet_address=models.CharField(max_length=200,null=True,blank=True,db_index=True)
    

    def __str__(self) -> str:
          return self.wallet_type_name
    

    