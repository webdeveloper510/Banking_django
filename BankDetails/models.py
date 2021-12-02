<<<<<<< HEAD
from django.db import models 
=======
from django.db import models
<<<<<<< HEAD
# from User.models import UserProfile
=======
from User.models import UserProfile
>>>>>>> afb13c41dbdb24802e00f00cbb6da2fc5fe8d7d0
>>>>>>> e7e0ca7df6e51c3d6bd5fffa7394623574400d61

# # Create your models here.

<<<<<<< HEAD
class UserProfile(models.Model):  
    # USERNAME_FIELD = 'username'
    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    accountnumber = models.CharField(max_length=200,default='')

    def __str__(self):  
          return  self.name  


=======
<<<<<<< HEAD
# class Bank(models.Model):
#     name = models.CharField(max_length=200,default='')
#     address = models.CharField(max_length=200,default='')
#     IFSC = models.CharField(max_length=200,default='')
#     BankCode = models.CharField(max_length=200,default='')
=======
>>>>>>> e7e0ca7df6e51c3d6bd5fffa7394623574400d61
class ForeignBank(models.Model):

    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
    rountingnumber = models.CharField(max_length=200,default='')
<<<<<<< HEAD
    username = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
=======
>>>>>>> afb13c41dbdb24802e00f00cbb6da2fc5fe8d7d0
>>>>>>> e7e0ca7df6e51c3d6bd5fffa7394623574400d61

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

<<<<<<< HEAD
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
=======
class Transanction(models.Model):
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Accountnumber= models.CharField(max_length=200,default='')
    FromBank = models.ForeignKey(LocalBank, on_delete=models.CASCADE,null=False,related_name='%(app_label)s_%(class)s_related')
    toBank = models.ForeignKey(ForeignBank, on_delete=models.CASCADE,null=False)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES, unique=True)

class UserBalance(models.Model):
    BankId = models.ForeignKey(LocalBank,on_delete=models.CASCADE)
    UserID = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
<<<<<<< HEAD
    AccountNumber= models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='AccountNumber')
    Balance = models.CharField(max_length=200,default=0)

=======
    AccountNumber= models.ForeignKey(Transanction,on_delete=models.CASCADE, related_name='AccountNumber')
    Balance = models.CharField(max_length=200)
>>>>>>> afb13c41dbdb24802e00f00cbb6da2fc5fe8d7d0
>>>>>>> e7e0ca7df6e51c3d6bd5fffa7394623574400d61
