from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View
from .models import *
from dashboard_app.models import *
from datetime import date,datetime
# Create your views here.
from django.contrib.auth.hashers import make_password
class Client_Registers(View):
    template_name="client/signup.html"
    country=Country.objects.all()
    context={'country':country}
    def get(self, request):
        return render(request,self.template_name,self.context)
    
    def post(self ,request):
        if request.method =="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            birthdate_str=request.POST.get('dob')
            username=request.POST.get('username')
            password=request.POST.get('pwd1')
            confrim_password=request.POST.get('pwd2')
            country=request.POST.get('country')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
        
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            age = (date.today() - birthdate).days // 365
            if age < 18:
              context={' birthdate_str': birthdate_str,'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'birth':'You must be at least 18 years old.','first_name':first_name,'last_name':last_name}
              return render(request,self.template_name,context)
            
            try:
                User.objects.get(username=username)
                context={'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'username_error':'User Already Exists...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            
            except User.DoesNotExist:
                  username=request.POST.get('username')
           
           
            try:
                User.objects.get(email=email)
                context={'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'email_error':'Email Already Exists...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            
            except User.DoesNotExist:
                  username=request.POST.get('username')
            #insert data
            if password!=confrim_password:
                context={'password':password,'confrim_password':confrim_password,'country':self.country,'password_error':'password does not match...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            else:
                instance=User.objects.create(first_name=first_name,last_name=last_name,username=username,password=make_password(password),email=email)
                Client_Register.objects.create(user=instance,first_name=first_name,last_name=last_name,email=email,mobile_no=mobile ,gender=gender, country=country,dob=birthdate_str,username=username,password=password)
                context={'sucess':"Singup form Register Successfully..",'country':self.country}
                return render(request,self.template_name,context)
        return render(request,self.template_name,self.context)
        


