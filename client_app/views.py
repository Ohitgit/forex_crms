from django.shortcuts import render,redirect
   
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    template_name="forex/index.html"
    def get(self, request):
        return render(request,self.template_name)

class Forex(View):
    template_name="forex/forex.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Commodities(View):
    template_name="forex/commodities.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Indices(View):
    template_name="forex/indices.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Stocks(View):
    template_name="forex/stocks.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Standard(View):
    template_name="forex/standard-account.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Pro(View):
    template_name="forex/pro.html"
    def get(self, request):
        return render(request,self.template_name)



class Institutional(View):
    template_name="forex/institutional.html"
    def get(self, request):
        return render(request,self.template_name)
    

class ZeroCommission(View):
    template_name="forex/zero-commission.html"
    def get(self, request):
        return render(request,self.template_name)


class Islamic(View):
    template_name="forex/islamic.html"
    def get(self, request):
        return render(request,self.template_name)
    


class Mini(View):
    template_name="forex/mini.html"
    def get(self, request):
        return render(request,self.template_name)
    

class Nano(View):
    template_name="forex/nano.html"
    def get(self, request):
        return render(request,self.template_name)


class Axion(View):
    template_name="forex/axion-trader.html"
    def get(self, request):
        return render(request,self.template_name)
    

class MetaTrader(View):
    template_name="forex/meta-trader.html"
    def get(self, request):
        return render(request,self.template_name)

class IntroducingBroker(View):
    template_name="forex/introducing-broker.html"
    def get(self, request):
        return render(request,self.template_name)


class AssetManager(View):
    template_name="forex/asset-manager.html"
    def get(self, request):
        return render(request,self.template_name)

    
class Whitelabel(View):
    template_name="forex/whitelabel.html"
    def get(self, request):
        return render(request,self.template_name)
    

class OurEdge(View):
    template_name="forex/ouredge.html"
    def get(self, request):
        return render(request,self.template_name)

    
class About(View):
    template_name="forex/about-us.html"
    def get(self, request):
        return render(request,self.template_name)



class Post(View):
    template_name="forex/post.html"
    def get(self, request):
        return render(request,self.template_name)

