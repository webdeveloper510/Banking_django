from django.db import models
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# # Create your models here.





class ForeignBank(models.Model):

    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")
    rountingnumber = models.CharField(max_length=9, default="")
    username = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200,default='')

    def __str__(self):

        return self.name


class LocalBank(models.Model):
    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    username = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")
    rountingnumber = models.CharField(max_length=9, default="")
    email = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ("pending", "pending"),
    ("confirmed", "confirmed"),
    ("completed", "completed"),
)


class UserProfile(models.Model):
    # USERNAME_FIELD = 'username'
    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    accountnumber = models.CharField(max_length=10, default="")
    bankId = models.ForeignKey(LocalBank, on_delete=models.CASCADE,max_length=10, default="")

    def __str__(self):

        return self.name


class Transaction(models.Model):
    Name = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False, blank=True
    )
    Accountnumber = models.CharField(max_length=10, default="")
    FromBank = models.ForeignKey(
        LocalBank,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        null=False,
        blank=True,
    )
    toBank = models.ForeignKey(
        ForeignBank, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")
    amount = models.FloatField(default=0)
    ForiegnBankrountingnumber = models.ForeignKey(
        ForeignBank,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        default="",
    )

    date = models.CharField(max_length=200)
    confirmdate = models.CharField(max_length=200)
    completeddate = models.CharField(max_length=200)


class UserBalance(models.Model):
    BankID = models.ForeignKey(
        LocalBank, on_delete=models.CASCADE, null=True, blank=True
    )
    UserId = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    AccountNumber = models.FloatField(default=0)
    Balance = models.CharField(max_length=200, default=0)
