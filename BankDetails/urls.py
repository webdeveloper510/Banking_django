from django.urls import path
from django.urls.resolvers import URLPattern
from .views import api_transaction,api_balance,localbank_register_request,login_page,add_client,edit_client

urlpatterns= [
    path('transaction/',api_transaction,name='test'),
    path('balance/',api_balance,name='balance'),
    path('localbank_Register/',localbank_register_request,name='localbank_Register'),
    path('login/',login_page,name='login'),
    path('addclient/',add_client,name='add_client'),
    path('editclient/<str:pk>',edit_client,name='edit_client')

]
