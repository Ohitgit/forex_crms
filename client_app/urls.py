
from django.urls import path

from .views import *

urlpatterns = [
    path('client',Client_Registers.as_view() ,name="signup"),
   



]
