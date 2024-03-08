
from django.urls import path

from .views import *

urlpatterns = [
    path('client',Client_Registers.as_view() ,name="signup"),
    path('signin',Signin.as_view() ,name="signin"),
    path('otp',Signup_Otp.as_view() ,name="otp"),
    path('forgototp',Forgot_Otp.as_view() ,name="forgototp"),
    path('forgot',Forgot.as_view() ,name="forgot"),
    path('changepassword/<str:token>',ChangePassword.as_view(), name='changepassword'),
    

    path('liveaccount',LiveAccount.as_view() ,name="liveaccount"),

]
