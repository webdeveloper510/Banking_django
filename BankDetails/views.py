from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transanction,UserBalance,LocalBank
from .serializers import TransactionSerializers,BalanceSerailizers
from django.contrib import messages
from django.contrib.auth import login
from User.models import UserProfile
from django.db import connection
from .forms import LocalBankForm 
# Create your views here.

@api_view(['GET'])
def api_transaction(request):
    transcation = Transanction.objects.all()
    serializer = TransactionSerializers(transcation,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_balance(request):
    balance = UserBalance.objects.all()
    serializers = BalanceSerailizers(balance,many=True)
    return Response(serializers.data)


def register_request(request):
	if request.method == "POST":
		form = LocalBankForm(request.POST or None)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = LocalBankForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})

def login_page(request):
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LocalBank.objects.get(username=username)
        if username ==  user.username:
            messages.success(request, "Login successfull." )
            return redirect('login')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'base/login.html')
