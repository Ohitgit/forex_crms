from django.shortcuts import render,redirect
from django.contrib import messages 
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import *
from dashboard_app.models import *
from datetime import date,datetime
from  .utils import *
import random
import json
import requests
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request,'clientapp/home.html')


class Client_register(View):
    country=Country.objects.all()
    context={'country':country}
    template_name="clientapp/client_register.html"
    def get(self, request):
        print(self.country)
        return render(request,self.template_name,self.context)
    
    def post(self ,request):
        if request.method =="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            # birthdate_str=request.POST.get('dob')
            username=request.POST.get('username')
            password=request.POST.get('pwd1')
            print('password',password)
            hasedpwd=make_password(password)
            confrim_password=request.POST.get('pwd2')
            country=request.POST.get('country')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            city=request.POST.get('city')
            zipcode=request.POST.get('zipcode')
            address=request.POST.get('address')
            state=request.POST.get('state')
        
            # birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            # age = (date.today() - birthdate).days // 365
            # if age < 18:
            #   context={' birthdate_str': birthdate_str,'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'birth':'You must be at least 18 years old.','first_name':first_name,'last_name':last_name}
            #   return render(request,self.template_name,context)
            
            try:
                User.objects.get(username=username)
                context={'confrim_password': confrim_password,'password':password,'zipcode':zipcode,'address':address,'state':state,'city':city,'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'username_error':'User Already Exists...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            
            except User.DoesNotExist:
                  username=request.POST.get('username')
           
           
            try:
                User.objects.get(email=email)
                context={'zipcode':zipcode,'address':address,'state':state,'city':city,'mobile':mobile,'email':email,'password':password,'confrim_password':confrim_password,'country':self.country,'email_error':'Email Already Exists...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            
            except User.DoesNotExist:
                  username=request.POST.get('username')
            #insert data
            if password!=confrim_password:
                context={'password':password,'confrim_password':confrim_password,'country':self.country,'password_error':'password does not match...','first_name':first_name,'last_name':last_name,'username':username}
                return render(request,self.template_name,context)
            else:
                instance=User.objects.create(first_name=first_name,last_name=last_name,username=username,password=hasedpwd,email=email)
                UploadDocument.objects.create(user=instance)
                Client_Register.objects.create(user=instance,first_name=first_name,last_name=last_name,email=email,mobile_no=mobile ,city=city,pincode=zipcode, country=country,username=username,password=password ,address=address,state=state)
               
                if Otp_Status.objects.filter(otp_status=False).exists():
                   return redirect('client_login')
                else:
                  otp = random.randint(100000, 999999)
                  request.session['otp']=otp
                  Util.user_email_verfication(request,instance,otp)
                  return redirect('otp')
               
        return render(request,self.template_name,self.context)
    
class Client_login(View):
    form = LoginForm()
    context={'form':form}
    template_name="clientapp/client_login.html"
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


class forgot_password(View):
    
    template_name="clientapp/forgot_password.html"
    def get(self, request):
        return render(request,self.template_name) 
    
    def post(self,request):
        if request.method == 'POST':
           
              email = request.POST.get('email')
             
              try:
                  user=User.objects.get(email=email)
                  print('user',user)
                  request.session['user']=user.id
                  otp = random.randint(100000, 999999)
                  request.session['otp']=otp
                  Util.user_email_verfication(request,user,otp)
                  return JsonResponse({'msg1':'successfully data'})
                  
              except User.DoesNotExist:
                   return JsonResponse({'msg':'Email Not Exists..'})
       
    

class auth_reset_password(View):
    template_name="clientapp/auth_reset_password.html"
    def get(self, request):
        return render(request,self.template_name) 



class Client_profile(View):
    
    template_name="clientapp/client_profile.html"
    def get(self, request):
        upload_document=UploadDocument.objects.get(user=request.user)
        profile=Client_Register.objects.get(user=request.user)
        context={'profile':profile,'upload_document':upload_document}
        return render(request,self.template_name,context)


class Open_live_account(View):
    template_name="clientapp/open_live_account.html"
    def get(self, request):
        return render(request,self.template_name)

class Open_demo_account(View):
    template_name="clientapp/open_demo_account.html"
    def get(self, request):
        return render(request,self.template_name)    



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
    
    
    def post(self,request):
        if request.method == 'POST':
            otp1=request.POST.get('otp')
            otp=request.session.get('otp')
            print(otp)
            print('otp1',otp1)
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
                  return JsonResponse({'msg1':'successfully data'})
            else:
                 return JsonResponse({'msg':'successfully data'})
             
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
    template_name="clientapp/auth_reset_password.html" 
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
                 return redirect('client_login')
        return render(request,self.template_name,self.context)

from django.contrib.auth.decorators import login_required
import requests

class LiveAccount(View):
    template_name="client/liveaccount.html"
    
    def get(self, request):
      user=Client_Register.objects.get(user=request.user)
      print('user',user)
      return render(request,self.template_name)
    
    def post(self,request):
      if request.method =="POST":
          forexgroup=request.POST.get('forex_group')
          leverage=request.POST.get('leverage')
          user=Client_Register.objects.get(user=request.user)
          print('user',user)
          url = "http://103.138.189.81/api/mt5/createLiveAccount"
          headers = {'Content-Type': 'application/json'}
          data={
              "ip": "43.228.124.119",
                "login": 313,
                "password": "Raz@1234",
                "name": user.first_name,
                "group": forexgroup,
                 "email": user.email,
                 "leverage":  leverage,
                 "main_password": "trade@1234",
                 "invest_password": "1234@trade",
                "phone_password": user.mobile_no,
                 "country": "India",
            
              }
          print('data',data)
          print('url',url)
          response_api = requests.post(url, headers=headers,json=data)
          json1= response_api.json()
          print('json1',json1)
          if response_api.status_code == 200:
            # LiveAccount.objects.create(ac_type=response_data.get('accountType'), cu_type=response_data.get('depositCurrency'),account_no=response_data.get('login'),user=request.user)
            return JsonResponse({'message': 'LiveAccount created successfully'}, status=200)
          else:
            return JsonResponse({'error': 'Failed to create LiveAccount'}, status=response_api.status_code)
          
      return render(request,self.template_name)



class deposit(View):
    template_name="clientapp/deposit.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class withdraw(View):
    template_name="clientapp/withdraw.html"
    def get(self, request):
        return render(request,self.template_name) 

class internal_transfer(View):
    template_name="clientapp/internal_transfer.html"
    def get(self, request):
        return render(request,self.template_name) 

class internal_transfer_report(View):
    template_name="clientapp/internal_transfer_report.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class deposit_report(View):
    template_name="clientapp/deposit_report.html"
    def get(self, request):
        return render(request,self.template_name) 

class withdraw_report(View):
    template_name="clientapp/withdraw_report.html"
    def get(self, request):
        return render(request,self.template_name)     




class Upadte_Information(View):
   
    def post(self, request):
        profile=Client_Register.objects.get(user=request.user)
        if request.method =="POST":
            profile.first_name=request.POST.get('first_name')  
            profile.last_name=request.POST.get('last_name')      
            profile.mobile_no=request.POST.get('mobile') 
            profile.save()
            return redirect('client_profile')



class Upadte_Residential(View):
   
    def post(self, request):
        profile=Client_Register.objects.get(user=request.user)
        if request.method =="POST":
            profile.pincode=request.POST.get('pincode')  
            profile.city=request.POST.get('city')      
            profile.state=request.POST.get('state') 
            profile.country=request.POST.get('country')
            profile.address=request.POST.get('address')
            profile.save()
            return redirect('client_profile')


class Change_Password(View):
   
    def post(self, request):
        user=User.objects.get(username=request.user)
        if request.method =="POST":
          
          new_password=request.POST.get('new_password')
          confirm_password=request.POST.get('confirm_password')
          if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return redirect('client_login')
            



class UpadteDoucment(View):
   
    def post(self, request):
        profile=UploadDocument.objects.get(user=request.user)
        if request.method =="POST":
            profile.documenttype=request.POST.get('document_type')  
                 
            profile.img=request.FILES.get('img') 
           
            profile.save()
            return redirect('client_profile')



class UpadteDoucment2(View):
   
    def post(self, request):
        profile=UploadDocument.objects.get(user=request.user)
        if request.method =="POST":
            profile.identitytype=request.POST.get('identitytype')  
            print(request.POST.get('identitytype')  )   
            profile.img2=request.FILES.get('img2') 
           
            profile.save()
            return redirect('client_profile')