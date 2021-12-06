from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from  BankDetails import views 
from User import views 

urlpatterns = [
    path('',include('BankDetails.urls')),
    path('',include('User.urls')),
    path('admin/', admin.site.urls),



]
