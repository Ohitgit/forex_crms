
from django.urls import path

from .views import *


urlpatterns = [
    
    path('all-client',Client_List.as_view() ,name="client_list"),
   
    path('client-profile/<int:id>',Client_profile.as_view() ,name="client_profile"),
    path('client_delete/<int:id>',Client_Delete.as_view(),name="client_delete"),
    path('client_update/<int:id>',ClientUpadteDoucment.as_view(),name="client_update"),
    path('client_updates/<int:id>',ClientUpadteDoucment2.as_view(),name="client_updates"),
    path('tradeaccount/<int:id>',TradeAccountupdate.as_view(),name="tradeaccount"),
    path('deposit_wallet/<int:id>',Deposit_Wallet.as_view(),name="Deposit_Wallet"),
    path('deposit-finance',Deposit_finance.as_view() ,name="deposit_finance"),
    path('withdraw-finance',Withdraw_finance.as_view() ,name="withdraw_finance"),

    path('deposit_reject/<int:id>',Deposit_Reject.as_view(),name="Deposit_Reject"),
    path('deposit_wallet/<int:id>',Deposit_Wallet.as_view(),name="Deposit_Wallet"),
    path('deposit-history',Deposit_History.as_view(),name="Deposit_History"),
    path('liveaccount',LiveAccounts.as_view(),name="LiveAccount"),
    path('demoaccount',DemoAccount.as_view(),name="DemoAccount"),
    path('liveacountdetailes/<int:id>',LiveAccountsDetailes.as_view(),name="liveacountdetailes"),
    path('demoacountdetailes/<int:id>',DemoAccountsDetailes.as_view(),name="demoacountdetailes"),
    path('liveusernameupdate/<int:id>',LiveUserNameUpdate.as_view(),name="LiveUserNameUpdate"),
    path('livegroupupdate/<int:id>',LiveGroupUpdate.as_view(),name="LiveGroupUpdate"),
    path('livepasswordupdate/<int:id>',LivePasswordUpdate.as_view(),name="LivePasswordUpdate"),
    path('dashboard-deposit',Dashboard_Deposittype.as_view(),name="Dashboard_Deposittype"),
    path('client_logins',Client_Login.as_view() ,name="client_logins"),
     path('update-leverage/<int:id>',Update_Leverage.as_view() ,name="Update_Leverage"),
]
