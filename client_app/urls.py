
from django.urls import path

from .views import *

urlpatterns = [
    path('',home ,name="home"),
    path('client-profile',Client_profile.as_view() ,name="client_profile"),
    path('client',Client_Registers.as_view() ,name="signup"),
    path('open-demo-account',Open_demo_account.as_view() ,name="open_demo_account"),
    path('open-live-account',Open_live_account.as_view() ,name="open_live_account"),

    path('client-register',Client_register.as_view() ,name="client_register"),
    path('client-login',Client_login.as_view() ,name="client_login"),

    path('client-forgot-password',forgot_password.as_view() ,name="forgot_password"),
    path('auth-reset-password',auth_reset_password.as_view() ,name="auth_reset_password"),

    path('signin',Signin.as_view() ,name="signin"),
    path('otp',Signup_Otp.as_view() ,name="otp"),
    path('forgototp',Forgot_Otp.as_view() ,name="forgototp"),
    path('forgot',Forgot.as_view() ,name="forgot"),
    path('changepassword/<str:token>',ChangePassword.as_view(), name='changepassword'),
]
