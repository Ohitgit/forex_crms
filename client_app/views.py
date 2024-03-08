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
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# Create your views here.

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
            hasedpwd=make_password(password)
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
                instance=User.objects.create(first_name=first_name,last_name=last_name,username=username,password=hasedpwd,email=email)
                Client_Register.objects.create(user=instance,first_name=first_name,last_name=last_name,email=email,mobile_no=mobile ,gender=gender, country=country,dob=birthdate_str,username=username,password=password)
                otp_staus=Otp_Status.objects.get(otp_status=False)
                print('otp_staus',otp_staus)
                if otp_staus:
                   return redirect('signin')
                else:
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
             
class Forgot_Otp(View):
    template_name="client/signupotp.html"
    def get(self, request):
        return render(request,self.template_name)
    
    def post(self,request):
        if request.method == 'POST':
            otp1=request.POST.get('otp')
            otp=request.session.get('otp')
            if int(otp) == int(otp1):
                  username=request.session.get('user')
                  obj=Client_Register.objects.get(user=username)
                  uuids=str(uuid.uuid4())
                  obj.uuid=uuids
                  obj.save()
                  current_site=get_current_site(request=request).domain
                  relativelink=reverse('changepassword',kwargs={'token':uuids})
                  absurl='http://'+current_site + relativelink
                  email_body='Hello, \n Use link below to reset your password  \n' + absurl
                  data={'email_body':email_body,'to_email':obj.email,'email_subject':'Reset your email'}
                  Util.forget_email(data)
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
                login(request,user)
                return redirect('home')
              else:
                 form = LoginForm()
                 context = {'error': 'Invalid credentials','form':form} 
                 return render(request,self.template_name,context)

import uuid
class Forgot(View):
    template_name="client/forgot.html"
    form=ForgotForm()
    print('form',form)
    context={'form':form}
    def get(self, request):
      return render(request,self.template_name,self.context)
    
    def post(self,request):
        if request.method == 'POST':
           form = ForgotForm(request.POST)
           if form.is_valid():
              email = form.cleaned_data['email']
              try:
                  user=User.objects.get(email=email)
                  print('user',user)
                  request.session['user']=user.id
                  otp = random.randint(100000, 999999)
                  request.session['otp']=otp
                  Util.user_email_verfication(request,user,otp)
                  return redirect('forgototp')
              except User.DoesNotExist:
                   form = ForgotForm(request.POST)
                   context={'error':'Email Not Exists..','form':form}
                   return render(request,self.template_name,context)
        return render(request,self.template_name,self.context)

class ChangePassword(View):
    template_name="client/changepassword.html"
    form=ChangePasswordForm()
    print('form',form)
    context={'form':form}
    def get(self, request,token):
      return render(request,self.template_name,self.context)
    def post(self ,request,token):
        if request.method == 'POST':
           form = ChangePasswordForm(request.POST)
           if form.is_valid():
              password = form.cleaned_data['password']
              confrimpassword = form.cleaned_data['confrimpassword']
              if password != confrimpassword:
                  messages.success(request, 'password not match')
                  current_url=request.get_full_path()
                  return redirect(current_url)
              else:
                 obj=Client_Register.objects.get(uuid=token)
                 print('update',obj)
                 user1=User.objects.get(id=obj.user.id)
                 print('user',user1)
                 user1.set_password(confrimpassword)
                 user1.save()
                 return redirect('signin')
        return render(request,self.template_name,self.context)