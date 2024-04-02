from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View
from .froms import *
from client_app.models import *
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
  