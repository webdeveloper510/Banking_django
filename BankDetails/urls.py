from django.urls import path
from django.urls.resolvers import URLPattern
from .views import api_transaction,api_balance

urlpatterns= [
    path('transaction/',api_transaction,name='test'),
    path('balance/',api_balance,name='balance')
]