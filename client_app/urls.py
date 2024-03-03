
from django.urls import path

from .views import *

urlpatterns = [
    path('',Home.as_view() ,name="home"),
    path('forex',Forex.as_view() ,name="forex"),
    path('commodities',Commodities.as_view() ,name="commodities"),
    path('indices',Indices.as_view() ,name="indices"),
    path('stocks',Stocks.as_view() ,name="stocks"),
    path('standard',Standard.as_view(),name="standard"),
    path('pro',Pro.as_view(),name="pro"),
    path('institutional',Institutional.as_view(),name="institutional"),
    path('zerocommission',ZeroCommission.as_view(),name="zerocommission"),
    path('islamic',Islamic.as_view(),name="islamic"),
    path('mini',Mini.as_view(),name='mini'),
    path('nano',Nano.as_view(),name='nano'),
    path('axion',Axion.as_view(),name='axion'),
    path('metatrader',MetaTrader.as_view(),name='metatrader'),
    path('introducingbroker',IntroducingBroker.as_view(),name="introducingbroker"),
    path('assetmanager',AssetManager.as_view(),name="assetmanager"),
    path('whitelabel',Whitelabel.as_view(),name="whitelabel"),
    path('ouredge',OurEdge.as_view(),name="ouredge"),
    path('about-us',About.as_view(),name="about-us"),
    path('post',Post.as_view(),name="post")



]
