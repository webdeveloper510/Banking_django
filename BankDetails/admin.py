from django.contrib import admin
from BankDetails.models import Bank, Transanction , UserBalance

# Register your models here.

admin.site.register(Bank)
admin.site.register(Transanction)
admin.site.register(UserBalance)