from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from  BankDetails import views as cv
from User import views as fv

urlpatterns = [
    path('',include('BankDetails.urls')),
    path('',include('User.urls')),
    path('admin/', admin.site.urls),



]
