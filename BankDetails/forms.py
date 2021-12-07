from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import LocalBank, UserProfile, Transaction,ForeignBank


class LocalBankForm(ModelForm):
    class Meta:
        model = LocalBank
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['name', 'address', 'Accountnumber',
                  'rountingnumber', 'username', 'password']

class ForiegnBankForm(ModelForm):
    class Meta:
        model = ForeignBank
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['name', 'address', 
                  'rountingnumber', 'username', 'password']

                  
class ClientForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class EditClientForm(forms.Form):

    name = forms.CharField()
    address = forms.CharField()
    AccountNumber = forms.CharField()


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        exclude = ('FromBank', 'ForiegnBankrountingnumber')
        fields = ['Accountnumber','Name','toBank','amount','status']


class StatusConfirmForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status']
