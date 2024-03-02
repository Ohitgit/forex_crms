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
      def __str__(self) -> str:
           return self.add_leverage_value


class Add_Currency(BaseModel):
      name=models.CharField(null=True,blank=True,db_index=True,max_length=200)
      def __str__(self) -> str:
           return self.name

        
class Add_Group(BaseModel):
    name=models.CharField(null=True,blank=True,db_index=True,max_length=200)

    def __str__(self) -> str:
           return self.name


class Create_Forex_Group(BaseModel):
     Account_type = (('live account', 'Live Account'), ('demo account', 'Demo Acount'),)
     account_name= models.CharField( max_length=20,choices=Account_type, default='live account',db_index=True)
     account_feture=models.CharField(max_length=200,null=True,blank=True,db_index=True)
     feture_value=models.CharField(max_length=200,null=True,blank=True,db_index=True)

     def __str__(self) -> str:
           return self.account_name
    


