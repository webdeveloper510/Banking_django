from django import forms
from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import LocalBank

# Create your forms here.

class LocalBankForm(UserCreationForm):
	class Meta:
		model = LocalBank
		# password = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'placeholder': 'alphanumeric password'}))
		
		fields = ['name','address','username','password','rountingnumber','Accountnumber']
