from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DeleteView
from django.http import HttpResponse
from django.views import View
from .froms import *
from client_app.models import *
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def forex_manager_ip():
    forex=Forex_Manager_Credential.objects.first()
    ip=forex.ip
    login=forex.login
    password=forex.password
    return ip,login,password

class Client_List(View):
    client_user=Client_Register.objects.all()
    context={'client_user':client_user}
    template_name="dashboard/client_list.html"
    def get(self, request):
        return render(request,self.template_name,self.context)  
      


class Client_profile(View):
    template_name="dashboard/client_profile1.html"
    def get(self, request,id):
        client_user=Client_Register.objects.get(id=id)
        live_account=LiveAccount.objects.filter(user=client_user.user)
        add_leverage=Add_Leverage.objects.all()
        context={'client_user':client_user,'live_account':live_account,'add_leverage':add_leverage}
        return render(request,self.template_name,context)
    
    def post(self, request, pk):
        # Retrieve the client object or return 404 if it doesn't exist
        client_user = get_object_or_404(Client_Register, id=pk)
        
        # Delete the client object
        client_user.delete()
        
        # Redirect to client list page after deletion
        return redirect('client_list')

   


class Client_Delete(View):
      def post(self, request, id):
        client_user = Client_Register.objects.get(id=id)
        client_user.delete()
        return redirect('client_list')
    



class ClientUpadteDoucment(View):
   
    def post(self, request,id):

        client_user=Client_Register.objects.get(id=id)
        profile=UploadDocument.objects.get(user=client_user.user)
        if request.method =="POST":
            profile.documenttype=request.POST.get('document_type')  
                 
            profile.img=request.FILES.get('img') 
           
            profile.save()
            messages.success(request, 'Doucment Upload Updated..')
            return redirect('client_profile',id )
        

    

class ClientUpadteDoucment2(View):
   
    def post(self, request,id):

        client_user=Client_Register.objects.get(id=id)
        profile=UploadDocument.objects.get(user=client_user.user)
        if request.method =="POST":
            profile.documenttype=request.POST.get('identitytype')  
                 
            profile.img=request.FILES.get('img') 
           
            profile.save()
            
            messages.success(request, 'Doucment Upload Updated..')
            return redirect('client_profile',id )




class TradeAccountupdate(View):
   
    def post(self, request,id):

        profile=Client_Register.objects.get(id=id)
       
        if request.method =="POST":
            profile.live_account_limit=request.POST.get('demo_accounts')  
                 
            profile.demo_account_limit=request.POST.get('live_accounts') 
           
            profile.save()
            
            messages.success(request, 'Trade Account Update..')
            return redirect('client_profile',id )


class Deposit_finance(View):
    template_name="dashboard/deposit_finance.html"

    def get(self, request):
        deposit=UserDeposits.objects.filter(status=False)
        context={'deposit':deposit}
        return render(request,self.template_name,context) 
        

class Withdraw_finance(View):
    template_name="dashboard/withdraw_finance.html"
    def get(self, request):
        return render(request,self.template_name)



class Deposit_History(View):
    template_name="dashboard/deposit_history.html"
    def get(self, request):
        deposit=UserDeposits.objects.filter(status=True)
        context={'deposit':deposit}
        return render(request,self.template_name,context)


class Deposit_Reject(View):
   
    def post(self, request,id):
        if request.method =="POST":
           remarks=request.POST.get('remarks')
           wallet=UserDeposits.objects.get(id=id)
           wallet.status=True
           wallet.reject=remarks
           wallet.save()
        return redirect('deposit_finance')



class Deposit_Wallet(View):
   
    def post(self, request,id):
        if request.method =="POST":
           wallet=UserDeposits.objects.get(id=id)
           client=Client_Register.objects.get(user=wallet.user)
           client.user_wallet+=wallet.amount
           client.save()
           wallet.status=True
           wallet.save()
        return redirect('deposit_finance')



class LiveAccounts(View):
    client_user=LiveAccount.objects.filter(group_name="liveaccount")
    context={'client_user':client_user}
    template_name="dashboard/liveaccount.html"
    def get(self, request):
        return render(request,self.template_name,self.context)

    
class DemoAccount(View):
    client_user=LiveAccount.objects.filter(group_name="demoaccount")
    context={'client_user':client_user}
    template_name="dashboard/demoaccount.html"
    def get(self, request):
        return render(request,self.template_name,self.context)




class LiveAccountsDetailes(View):
   
    template_name="dashboard/liveaccountdetailes.html"
    def get(self, request,id):
        client_user=LiveAccount.objects.get(id=id)
        context={'client_user':client_user}
        return render(request,self.template_name,context)


class DemoAccountsDetailes(View):
   
    template_name="dashboard/demoaccountdetailes.html"
    def get(self, request,id):
        client_user=LiveAccount.objects.get(id=id)
        context={'client_user':client_user}
        return render(request,self.template_name,context)




class LiveUserNameUpdate(View):
   
    def post(self, request,id):
    
        if request.method =="POST":
           name_id=request.POST.get('name')
           print(name_id)
           name=request.POST.get('account_name')
           print('name',name)
           client=LiveAccount.objects.get(user__username=name_id)
           
          
           client.user.username=name
           client.user.save()
        return redirect('liveacountdetailes',id)

    

class LiveGroupUpdate(View):
   
    def post(self, request,id):
    
        if request.method =="POST":
          name=request.POST.get('account_group')
          print('name',name)
          client=LiveAccount.objects.get(id=id)
          client.group=name
          print(client.save())
        return redirect('liveacountdetailes',id)



class LivePasswordUpdate(View):
   
    def post(self, request,id):
    
        if request.method =="POST":
          select=request.POST.get('select')
          password=request.POST.get('password')
         
          client=LiveAccount.objects.get(id=id)
         
        return redirect('liveacountdetailes',id)


class  Dashboard_Deposittype(View):
        def post(self,request):
            if request.method == 'POST':
              account_no=request.POST.get('account_no')
              amount=request.POST.get('amount')
              comment=request.POST.get('comment')
              url = "http://103.138.189.81/api/mt4/depostLiveAccount"
              ip,login,password=forex_manager_ip()
              deposit_api="{\r\n    \"ip\":\""+ip+"\",\r\n    \"login\":"+str(login)+",\r\n    \"password\":\""+password+"\",\r\n    \"account_login\":"+account_no+",\r\n    \"amount\": "+str(amount)+",\r\n    \"comment\": \"Deposit\"\r\n}"
              headers = {
                    'Content-Type': 'application/json'
               }
              response = requests.request("POST", url, headers=headers, data=deposit_api)
              print(response.text)
              url1 = "http://103.138.189.81/api/mt4/getLiveTradeAccountDetails"
              payload="{\r\n      \"ip\":\""+ip+"\",\r\n    \"login\":"+login+",\r\n    \"password\":\""+password+"\",\r\n    \"account_login\":"+account_no+"\r\n}"
              headers = { 'Content-Type': 'application/json' }
              response1 = requests.request("POST", url1, headers=headers, data=payload)
            return redirect('Client_profile')




#admin withdraw
class  Dashboard_Wihdrawtype(View):
        def post(self,request):
            if request.method == 'POST':
              account_no=request.POST.get('account_no')
              amount=request.POST.get('amount')
              comment=request.POST.get('comment')
              url = "http://103.138.189.81/api/mt4/withdrawLiveAccount"
              ip,login,password=forex_manager_ip()
              payload="{\r\n    \"ip\":\""+ip+"\",\r\n    \"login\":"+str(login)+",\r\n    \"password\":\""+username+"\",\r\n    \"account_login\":"+str(account_no)+",\r\n    \"amount\": "+str(amount)+",\r\n    \"comment\": \"Withdraw\"\r\n}"
              headers = {'Content-Type': 'application/json'}
              url1 = "http://103.138.189.81/api/mt4/getLiveTradeAccountDetails"
              payload1="{\r\n      \"ip\":\""+ip+"\",\r\n    \"login\":"+str(login)+",\r\n    \"password\":\""+username+"\",\r\n    \"account_login\":"+str(account_no)+"\r\n}"
              headers = {'Content-Type': 'application/json'}
              response1 = requests.request("POST", url1, headers=headers, data=payload1)
              print(response1.text)
              deposit_live=json.loads(response1.text.encode("utf-8"))




class Client_Login(View):
    def post(self,request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                 print('okk')
                 return redirect('client_list')
            
            else:
                return redirect('home')





class Update_Leverage(View):   
    def post(self,request,id):
       obj1=Client_Register.objects.get(id=id)
       if request.method == 'POST':
            mt5_login=request.POST.get('account_no')
            leverage=request.POST.get('leverage')
            
            print('------leverag kkk e-----',leverage)
            url = "http://103.138.189.81/api/mt4/updateLiveAccountLeverage"
            ip,login,password=forex_manager_ip()
            payload="{\r\n   \"ip\":\""+ip+"\",\r\n    \"login\":"+str(login)+",\r\n    \"password\":\""+password+"\",\r\n    \"account_login\":"+mt5_login+",\r\n    \"leverage\":\" "+str(leverage)+"\"\r\n}"
            # payload="{\r\n    \"ip\":\""+ip+"\",\r\n    \"login\":"+str(login)+",\r\n    \"password\":\""+username+"\",\r\n    \"account_login\":"+mt5_login+",\r\n    \"leverage\": "+str(leverage)+"\r\n}"
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            lev=Add_Leverage.objects.get(add_leverage_value=leverage)
            
            obj1.leverage_id=lev.id
            obj1.save()
            messages.success(request,'update leverage successful')
            return redirect('client_profile',id)