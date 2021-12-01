from django.db import models
from User.models import UserProfile

# Create your models here.

class ForeignBank(models.Model):

    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
    rountingnumber = models.CharField(max_length=200,default='')

class LocalBank(models.Model):
    USERNAME_FIELD = 'username'
    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    username = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
    rountingnumber = models.CharField(max_length=200,default='')
    Accountnumber= models.CharField(max_length=200,default='')
    

STATUS_CHOICES = (
    ('completed', 'completed'),
    ('pending', 'pending'),
)

class Transanction(models.Model):
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Accountnumber= models.CharField(max_length=200,default='')
    FromBank = models.ForeignKey(LocalBank, on_delete=models.CASCADE,null=False,related_name='%(app_label)s_%(class)s_related')
    toBank = models.ForeignKey(ForeignBank, on_delete=models.CASCADE,null=False)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES, unique=True)



class UserBalance(models.Model):
    BankId = models.ForeignKey(LocalBank,on_delete=models.CASCADE)
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    AccountNumber= models.ForeignKey(Transanction,on_delete=models.CASCADE, related_name='AccountNumber')
    Balance = models.CharField(max_length=200)