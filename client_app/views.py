from django.shortcuts import render,redirect
from django.contrib import messages 
from django.http import HttpResponse
from django.views import View
from .models import *
from dashboard_app.models import *
from datetime import date,datetime
from  .utils import *
import random
from .forms import *
from django.contrib.auth import authenticate, login, logout
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
                otp = random.randint(100000, 999999)
                request.session['otp']=otp
                Util.user_email_verfication(request,instance,otp)
                return redirect('otp')
               
        return render(request,self.template_name,self.context)



class Signup_Otp(View):
    template_name="client/signupotp.html"
    def get(self, request):
        return render(request,self.template_name)
    
    def post(self,request):
        if request.method == 'POST':
            otp1=request.POST.get('otp')
            otp=request.session.get('otp')
            if int(otp) == int(otp1):
              messages.success(request, 'Email Verify Succesfully..')
              return redirect('signin')
            else:
                 messages.success(request, ' Please valid Email..')
                 return redirect('otp')
             

class Signin(View):
    template_name="client/signin.html"
    form = LoginForm()
    context={'form':form}
    def get(self, request):
      return render(request,self.template_name,self.context)
    
    def post(self,request):
        if request.method == 'POST':
           form = LoginForm(request.POST)
           if form.is_valid():
              username = form.cleaned_data['username']
              password = form.cleaned_data['password']
              user = authenticate(request, username=username, password=password)
              if user is not None:
                return redirect('home')
              else:
                 form = LoginForm()
                 context = {'error': 'Invalid credentials','form':form} 
                 return render(request,self.template_name,context)
             