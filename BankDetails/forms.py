from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import LocalBank, UserProfile, Transaction


class LocalBankForm(ModelForm):
    class Meta:
        model = LocalBank
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['name', 'address', 'Accountnumber',
                  'rountingnumber', 'username', 'password']


class ClientForm(forms.Form):
    class Meta:
        name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'name'}))
        address = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'address'}))
        accountnumber = forms.IntegerField()


class EditClientForm(forms.Form):
    class Meta:
        name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'name'}))
        address = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'address'}))


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class StatusConfirmForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status']
