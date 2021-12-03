from django.contrib import admin
from BankDetails.models import LocalBank, ForeignBank, Transaction, UserBalance, UserProfile

# Register your models here.

admin.site.register(LocalBank)
admin.site.register(ForeignBank)
admin.site.register(Transaction)
admin.site.register(UserBalance)
admin.site.register(UserProfile)
