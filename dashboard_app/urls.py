
from django.urls import path

from .views import *


urlpatterns = [
    
    path('all-client',Client_List.as_view() ,name="client_list"),
    path('client-profile/<int:id>',Client_profile.as_view() ,name="client_profile"),

]
