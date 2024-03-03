from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View
from .froms import *
# Create your views here.
class Home(View):
    template_name="dashboard/index.html"
    form=AddGroupForm()
    def get(self, request):
        print(self,'self')
        
        context={'form':self.form}
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')