from django.contrib import admin
from BankDetails.models import Bank, Transanction_model 

# Register your models here.

admin.site.register(Bank)
admin.site.register(Transanction_model)
# admin.site.register(UserBalance)