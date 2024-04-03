
from django.urls import path

from .views import *


urlpatterns = [
    
    path('all-client',Client_List.as_view() ,name="client_list"),
    path('client-profile/<int:id>',Client_profile.as_view() ,name="client_profile"),
    path('client_delete/<int:id>',Client_Delete.as_view(),name="client_delete"),
    path('client_update/<int:id>',ClientUpadteDoucment.as_view(),name="client_update"),
    path('client_updates/<int:id>',ClientUpadteDoucment2.as_view(),name="client_updates")

]
