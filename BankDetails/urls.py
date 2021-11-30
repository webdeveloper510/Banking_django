from django.urls import path
from django.urls.resolvers import URLPattern
from .views import api_test

urlpatterns= [
    path('test/',api_test,name='test'),
]