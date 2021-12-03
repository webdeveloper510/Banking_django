
from django.db import models
from django.db import models

# # Create your models here.


class UserProfile(models.Model):
    # USERNAME_FIELD = 'username'
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    accountnumber = models.CharField(max_length=200, default='')


def __str__(self):
    return str(self.name)


class ForeignBank(models.Model):

    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    rountingnumber = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')

    def __str__(self):

        return self.name


class LocalBank(models.Model):
    USERNAME_FIELD = 'username'
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    rountingnumber = models.CharField(max_length=9, default='')
    Accountnumber = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('completed', 'completed'),

)


class Transaction(models.Model):
    UserID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Accountnumber = models.CharField(max_length=200, default='')
    FromBank = models.ForeignKey(LocalBank, on_delete=models.CASCADE,
                                 null=False, related_name='%(app_label)s_%(class)s_related')
    toBank = models.ForeignKey(
        ForeignBank, on_delete=models.CASCADE, null=False)
    status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, unique=True)
    amount = models.FloatField(default=0)


class UserBalance(models.Model):
    BankID = models.ForeignKey(LocalBank, on_delete=models.CASCADE)
    UserId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    AccountNumber = models.FloatField(default=0)
    Balance = models.CharField(max_length=200)

    def __str__(self):
        return self.UserId
