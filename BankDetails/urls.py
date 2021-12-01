from django.urls import path
from django.urls.resolvers import URLPattern
from .views import api_transaction,api_balance
from .views import register_request,login_page

urlpatterns= [
    path('transaction/',api_transaction,name='test'),
    path('balance/',api_balance,name='balance'),
    path('client_Register/',register_request,name='client_Register'),
    path('login/',login_page,name='login'),

]