from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from  BankDetails import views as cv
from User import views as fv

urlpatterns = [
    path('',include('BankDetails.urls')),
    path('',include('User.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', cv.bank_detail,name='bank_detail'),
    url(r'^userdata/$', fv.user_detail, name='user_detail'),


]
