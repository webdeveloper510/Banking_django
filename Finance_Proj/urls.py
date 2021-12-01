from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('BankDetails.urls')),
    path('',include('User.urls')),
    path('admin/', admin.site.urls),
]
