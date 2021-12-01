from django.contrib import admin
from BankDetails.models import LocalBank,ForeignBank, Transanction ,UserBalance

# Register your models here.

admin.site.register(LocalBank)
admin.site.register(ForeignBank)
admin.site.register(Transanction)
admin.site.register(UserBalance)