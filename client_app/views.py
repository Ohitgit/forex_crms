from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    template_name="forex/index.html"
    def get(self, request):
        return render(request,self.template_name)

