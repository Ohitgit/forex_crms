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
import uuid
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib import messages
from dashboard_app.models import *

# Create your views here.
def forex_manager_ip():
     pass
# def forex_manager_ip():
#     forex=None
#     ip=forex.ip
#     login=forex.login
#     password=forex.password
#     return ip,login,password

def home(request):
    wallet_amount=Client_Register.objects.get(user=request.user)
    context={'wallet_amount':wallet_amount}
    return render(request,'clientapp/home.html',context)


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
    print('yes---------')
    forex_group=Forex_Group.objects.all()
    leverage= Add_Leverage.objects.all()
    demo=LiveAccount.objects.filter(group="pro/micro")
    # ip,login,password=forex_manager_ip()
    context={'forex_group':forex_group,'leverage':leverage,'demo':demo}
    template_name="clientapp/open_live_account.html"
    def get(self, request):
        return render(request,self.template_name,self.context)
    
    def post(self,request):
      
      if request.method =="POST":
          forexgroup=request.POST.get('forex_group')
          leverage=request.POST.get('leverage')
          user=Client_Register.objects.get(user=request.user)
          print('user',user)
          url = "http://103.138.189.81/api/mt5/createLiveAccount"
          headers = {'Content-Type': 'application/json'}
          data={
              "ip": self.ip,
                "login": self.login,
                "password": self.password,
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
          response_data= response_api.json()
          print('json1',response_data)
          if response_data['status'] == True:
            LiveAccount.objects.create(group=data['group'],login=response_data.get('login'),email=data['email'],password=data['password'],user=request.user,leverage=data['leverage'],group_name="liveaccount")
           
            return redirect('open_live_account')
            # return JsonResponse({'message': 'LiveAccount created successfully'}, status=200)
          else:
            return JsonResponse({'error': 'Failed to create LiveAccount'}, status=response_api.status_code)
          
      return render(request,self.template_name,self.context) 

class Open_demo_account(View):

    template_name="clientapp/open_demo_account.html"
    forex_group=Forex_Group.objects.all()
    leverage= Add_Leverage.objects.all()
    # ip,login,password=forex_manager_ip()
    demo=LiveAccount.objects.filter(group_name="demoaccount")
    context={'forex_group':forex_group,'leverage':leverage,'demo':demo}
    def get(self, request):
        return render(request,self.template_name,self.context)
    def post(self,request):
      if request.method =="POST":
          forexgroup=request.POST.get('forex_group')
          leverage=request.POST.get('leverage')
          user=Client_Register.objects.get(user=request.user)
          print('user',user)
          url = "http://103.138.189.81/api/mt5/createLiveAccount"
          headers = {'Content-Type': 'application/json'}
          data={
              "ip": self.ip,
                "login": self.login,
                "password": self.password,
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
          response_data= response_api.json()
          print('json1',response_data)
          if response_data['status'] == True:
            
            LiveAccount.objects.create(group=data['group'],login=response_data.get('login'),email=data['email'],password=data['password'],user=request.user,leverage=data['leverage'],group_name="demoaccount")
            return redirect('open_demo_account')
            # return JsonResponse({'message': 'LiveAccount created successfully'}, status=200)
          else:
            return JsonResponse({'error': 'Failed to create LiveAccount'}, status=response_api.status_code)
          
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



def genrate_transcationid():
    return str(uuid.uuid4())[:8]

class deposit(View):
    template_name="clientapp/deposit.html"
    live=LiveAccount.objects.filter(group_name='liveaccount')
    bank=Bank_Detail.objects.first()
    deposit=Usdt.objects.all()
       
    context={'live':live,'bank':bank,'deposit':deposit}
    def get(self, request):
        return render(request,self.template_name,self.context) 
    def post(self,request):
        ip = request.META.get('REMOTE_ADDR')
       
        trade_account=request.POST.get('trade_account_number')
        amount=float(request.POST.get('amount'))
        deposit_type=request.POST.get('deposit_type')
        recipet=request.FILES.get('file')
        usdt_address=request.POST.get('usdt_type')
        comment=request.POST.get('comment')
       
        if amount > 0:
          UserDeposits.objects.create(usdt_address=usdt_address,user=request.user,action_choice=trade_account,amount=amount,deposit_from=deposit_type,recipet=recipet,comment=comment,transaction_ID=genrate_transcationid(),ip_address=ip)
          messages.success(request, 'Deposit Inserted Successfully...')
        else:
              messages.success(request, 'insfufision balance ..')
              return render(request,self.template_name,self.context) 
        
        return render(request,self.template_name,self.context) 
    
class withdraw(View):
    template_name="clientapp/withdraw.html"
    def get(self, request):
        return render(request,self.template_name) 

class internal_transfer(View):
    
    demo=LiveAccount.objects.filter(group_name="liveaccount")
    # ip,login,password=forex_manager_ip()
    internal_transfer=Internal_Transfer.objects.all()
    
    context={'demo':demo,'internal_transfer':internal_transfer}

    template_name="clientapp/internal_transfer.html"
    def get(self, request):
       
        return render(request,self.template_name,self.context) 
    def post(self,request):
        user_wallets=Client_Register.objects.get(user=request.user)
        # ip,login,password=forex_manager_ip()
        if request.method == "POST":
          transfer_from=request.POST.get('transfer_from')
          transfer_to=request.POST.get('transfer_to')
          
          if  transfer_from ==  transfer_to:
              demo=LiveAccount.objects.filter(group_name="liveaccount")
              internal_transfer=Internal_Transfer.objects.all()
              context={'demo':demo,'internal_transfer':internal_transfer,'error':'Same account selected. Please choose a different wallet type '}
              return render(request,self.template_name,context)
              

          amount=int(request.POST.get('amount'))                                                                                                                                                                                         
          url = "http://103.138.189.81/api/mt5/depostLiveAccount"
          headers = {'Content-Type': 'application/json'}
          data={
              "ip": ip,
                "login": login,
                "password": password,
                "account_login":transfer_from,
                 "amount": amount,
                "comment": "test deposit"
          }
          print('data',data)
          print('url',url)
          response_api = requests.post(url, headers=headers,json=data)
          response_data= response_api.json()
          print('json1',response_data)
          if response_data['status'] == True and amount > 0 and user_wallets.user_wallet > 0 :
              minusamount=user_wallets.user_wallet-amount
              user_wallets.user_wallet=minusamount
              user_wallets.save()
              Internal_Transfer.objects.create(transfer_from=transfer_from,transfer_to=transfer_to, amount= amount, transaction_id=response_data['data']['transaction_id'])
              messages.success(request, 'Internal Transfer Successfully...')
          else:
               messages.success(request, 'Somewthing Went ...')
        return render(request,self.template_name,self.context)    

class internal_transfer_report(View):
    demo=LiveAccount.objects.filter(group="pro/micro")
    context={'demo':demo}
    template_name="clientapp/internal_transfer_report.html"
    def get(self, request):
        return render(request,self.template_name,self.context) 
    
class deposit_report(View):
    template_name="clientapp/deposit_report.html"
    def get(self, request):
        deposit=UserDeposits.objects.all()
        context={'deposit':deposit}
        return render(request,self.template_name,context) 

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
            profile.gender=request.POST.get('gender') 
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
            messages.success(request, 'Doucment Upload Updated..')
            return redirect('client_profile')



class UpadteDoucment2(View):
   
    def post(self, request):
        profile=UploadDocument.objects.get(user=request.user)
        if request.method =="POST":
            profile.identitytype=request.POST.get('identitytype')  
            print(request.POST.get('identitytype')  )   
            profile.img2=request.FILES.get('img2') 
           
            profile.save()
            messages.success(request, 'Doucment Upload Updated..')
            return redirect('client_profile')



class EmailVerfiy(View):
   
    def post(self, request):
       
        if request.method =="POST":
            email=request.POST.get('email') 
            otp = random.randint(100000, 999999)
            request.session['emailotp']=otp
            Util.email_verfication(request,email,otp)
            return JsonResponse({'msg':"otp send"})



class Email_Otp(View):
    
    
    def post(self,request):
        if request.method == 'POST':
            otp1=request.POST.get('otp')
            otp=request.session.get('emailotp')
            email_status=Client_Register.objects.get(user=request.user)
            print('email_status',email_status)

            print('otp1',otp1)
            if int(otp) == int(otp1):
                email_status.email_status=True
                email_status.save()
                return JsonResponse({'msg':"otp send"})
            else:
                return JsonResponse({'msg1':"otp invalid otp"})
            





class DepositOtp(View):
       def post(self,request):
        user=User.objects.get(username=request.user)
        if request.method == 'POST':
            otp = random.randint(100000, 999999)
            request.session['otp1']=otp
            print('otp',otp)
            Util.depositotp(request,user,otp)
            return JsonResponse({'msg':'otp request send'})


class DepositOtpverfiy(View):
       def post(self,request):
       
        if request.method == 'POST':
            otp1 =request.session.get('otp1')
            otp=request.POST.get('otp')
            if int(otp1) == int(otp):
             return JsonResponse({'msg':'otp verfiy'})
            else:
                return JsonResponse({'msg1':'otp not verfiy'})
