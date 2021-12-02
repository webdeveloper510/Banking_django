from django import forms
from django.forms import ModelForm
from .models import LocalBank ,UserProfile

class LocalBankForm(ModelForm):
    class Meta:
        model = LocalBank
        widgets = {
        'password': forms.PasswordInput(),
         }
        fields = ['name', 'address', 'Accountnumber','rountingnumber', 'username','password']


# class LocalBankForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
#     address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address'}))
#     accountnumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Account Number'}))
#     routingnumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Routing Number'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
#     password = forms.CharField(widget=forms.PasswordInput())

class ClientForm(forms.Form):
    class Meta:
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
        address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address'}))
        accountnumber = forms.IntegerField()

class EditClientForm(forms.Form):
    class Meta:
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
        address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address'}))
