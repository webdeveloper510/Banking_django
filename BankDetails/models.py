from django.db import models
from User.models import UserProfile

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    IFSC = models.CharField(max_length=200,default='')
    BankCode = models.CharField(max_length=200,default='')

STATUS_CHOICES = (
    ('completed', 'completed'),
    ('pending', 'pending'),
)

class Transanction_model(models.Model):
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Accountnumber= models.CharField(max_length=200,default='')
    Type = models.CharField(max_length=200,default='')
    FromBank = models.OneToOneField(Bank,on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    # toBank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES, unique=True)



class UserBalance(models.Model):
    BankId = models.ForeignKey(Bank,on_delete=models.CASCADE)
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    AccountNumber= models.ForeignKey(Transanction_model,on_delete=models.CASCADE, related_name='AccountNumber')
    Balance = models.CharField(max_length=200)