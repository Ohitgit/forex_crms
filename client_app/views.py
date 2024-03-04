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

