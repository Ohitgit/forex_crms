from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View
from .models import *
from datetime import date,datetime
# Create your views here.

class Client_Registers(View):
    template_name="client/form.html"
    def get(self, request):
        return render(request,self.template_name)
    
    def post(self ,request):
        if request.method == 'POST':
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            pincode=request.POST.get('pincode')
            birthdate_str=request.POST.get('birth')
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            age = (date.today() - birthdate).days // 365
            
              
               
               
            try:
                user=User.objects.get(username=username)
                
                if user:
                  context={'username_error':'User Already Exists...','first_name':first_name,'last_name':last_name,'username':username}
                  return render(request,self.template_name,context)
               
            except User.DoesNotExist:
                  username=request.POST.get('username')
                  
            if age < 18 :
                 context={'birth':'You must be at least 18 years old.','first_name':first_name,'last_name':last_name,'username':username}
                 return render(request,self.template_name,context)
            user_instansce=User.objects.create(username=username)
            client_instance=Client_Register.objects.create(user=user_instansce,first_name=first_name,last_name=last_name,username=username,pincode=pincode)
          
            context={'username_sucess':'Registration Successfully ...'}
            return render(request,self.template_name,context)
class Home(View):
    template_name="forex/index.html"
    def get(self, request):
        return render(request,self.template_name)

class Forex(View):
    template_name="forex/forex.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Commodities(View):
    template_name="forex/commodities.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Indices(View):
    template_name="forex/indices.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Stocks(View):
    template_name="forex/stocks.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Standard(View):
    template_name="forex/standard-account.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Pro(View):
    template_name="forex/pro.html"
    def get(self, request):
        return render(request,self.template_name)



class Institutional(View):
    template_name="forex/institutional.html"
    def get(self, request):
        return render(request,self.template_name)
    

class ZeroCommission(View):
    template_name="forex/zero-commission.html"
    def get(self, request):
        return render(request,self.template_name)


class Islamic(View):
    template_name="forex/islamic.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Mini(View):
    template_name="forex/mini.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Nano(View):
    template_name="forex/nano.html"
    def get(self, request):
        return render(request,self.template_name)


class Axion(View):
    template_name="forex/axion-trader.html"
    def get(self, request):
        return render(request,self.template_name)
    

class MetaTrader(View):
    template_name="forex/meta-trader.html"
    def get(self, request):
        return render(request,self.template_name)

class IntroducingBroker(View):
    template_name="forex/introducing-broker.html"
    def get(self, request):
        return render(request,self.template_name)


class AssetManager(View):
    template_name="forex/asset-manager.html"
    def get(self, request):
        return render(request,self.template_name)

    
class Whitelabel(View):
    template_name="forex/whitelabel.html"
    def get(self, request):
        return render(request,self.template_name)
    

class OurEdge(View):
    template_name="forex/ouredge.html"
    def get(self, request):
        return render(request,self.template_name)

    
class About(View):
    template_name="forex/about-us.html"
    def get(self, request):
        return render(request,self.template_name)



class Post(View):
    template_name="forex/post.html"
    def get(self, request):
        return render(request,self.template_name)

