<<<<<<< HEAD
from django.http import HttpResponse

# Create your views here.

def bank_detail(request):
    return('detail')

    
=======
from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transanction,UserBalance,LocalBank,UserProfile,UserBalance
from .serializers import TransactionSerializers,BalanceSerailizers
from django.contrib import messages
from django.contrib.auth import login
from django.db import connection
from .forms import LocalBankForm,ClientForm,EditClientForm
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


def localbank_register_request(request):
	if request.method == "POST":
		form = LocalBankForm(request.POST or None)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successfull." )
			return redirect("localbank_Register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = LocalBankForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})

def login_page(request):
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LocalBank.objects.get(username=username)
        request.session['localbankid']= user.id
        if username ==  user.username:
            messages.success(request, "Login successfull." )
            return redirect('login')
        else:
            messages.error(request, "Invalid Credentials")
<<<<<<< HEAD
    return render(request,'base/login.html',context={"register_form":user})


def add_client(request):
    localbankid = request.session.get('localbankid')
    if request.method == 'POST':
        clients = ClientForm(request.POST or None)
        if clients.is_valid():
            clients.save()
            clientid = clients.id
            messages.success(request, "Client created  successfully." )
            balance = UserBalance(AccountNumber=request.POST['accountnumber'],BankId=localbankid,UserID=clientid)
            balance.save()
            return redirect('addclient')
        messages.error(request, "Something went wrong !!")
    clients = ClientForm()
    return render(request,'base/ad_client.html')

def edit_client(request,pk):
    if request.method=='POST':
        editform = EditClientForm(request.POST or None)
        if editform.is_valid():
            data = UserProfile.objects.filter(id=pk).update(editform)
            context = {
                'data':data,
            }
            messages.success(request, "Client created  successfully." )
    return render(request,'base/editclient.html',context)




=======
    return render(request,'base/login.html')
>>>>>>> afb13c41dbdb24802e00f00cbb6da2fc5fe8d7d0
>>>>>>> e7e0ca7df6e51c3d6bd5fffa7394623574400d61
