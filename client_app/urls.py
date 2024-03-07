
from django.urls import path

from .views import *

urlpatterns = [
    path('client',Client_Registers.as_view() ,name="signup"),
    path('signin',Signin.as_view() ,name="signin"),
    path('otp',Signup_Otp.as_view() ,name="otp"),
]
