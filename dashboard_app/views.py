from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DeleteView
from django.http import HttpResponse
from django.views import View
from .froms import *
from client_app.models import *
from django.contrib import messages
# Create your views here.


class Client_List(View):
    client_user=Client_Register.objects.all()
    context={'client_user':client_user}
    template_name="dashboard/client_list.html"
    def get(self, request):
        return render(request,self.template_name,self.context)    


class Client_profile(View):
    template_name="dashboard/client_profile.html"
    def get(self, request,id):
        client_user=Client_Register.objects.get(id=id)
        context={'client_user':client_user}
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



class Deposit_finance(View):
    template_name="dashboard/deposit_finance.html"
    def get(self, request):
        return render(request,self.template_name) 
        

class Withdraw_finance(View):
    template_name="dashboard/withdraw_finance.html"
    def get(self, request):
        return render(request,self.template_name)