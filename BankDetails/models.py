from django.db import models 

# # Create your models here.

# class Bank(models.Model):
#     name = models.CharField(max_length=200,default='')
#     address = models.CharField(max_length=200,default='')
#     IFSC = models.CharField(max_length=200,default='')
#     BankCode = models.CharField(max_length=200,default='')



# class Transanction(models.Model):
#     UserID = models.ForeignKey(User,on_delete=models.CASCADE)
#     BankId = models.ForeignKey(Bank)
#     AccountNumber= models.CharField(max_length=200,default='')
#     Type = models.CharField(max_length=200,default='')
#     FromBank = models.CharField(max_length=200,default='')
#     ToBank = models.CharField(max_length=200)


# class UserBalance(models.Model):
#     BankID = models.ForeignKey(Transanction,on_delete=models.CASCADE)
#     UserId = models.ForeignKey(Bank,on_delete=models.CASCADE)
#     AccountNumber= models.ForeignKey(Bank,on_delete=models.CASCADE)
#     Balance = models.CharField(max_length=200)