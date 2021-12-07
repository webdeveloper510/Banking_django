from django import http
from django.core.exceptions import EmptyResultSet
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import Transaction, UserBalance, LocalBank, UserProfile, UserBalance,ForeignBank
from .serializers import TransactionSerializers, BalanceSerailizers
from django.contrib import messages
from django.contrib.auth import login
from django.db import connection
from .forms import LocalBankForm, ClientForm, EditClientForm, TransactionForm, StatusConfirmForm,ForiegnBankForm
from django.core.mail import EmailMultiAlternatives
from rest_framework.test import force_authenticate
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your views here.

def localbank_register_request(request):
  
  
    try:
        form = None
        if request.is_ajax and request.method == "POST":
             #print(request.POST['username'])
             
            myDict = dict(zip(request.POST.keys(), request.POST.values()))
            del myDict['csrfmiddlewaretoken']
            form = LocalBank(**myDict)
            instance = form.save()
            return JsonResponse({"instance": "instance"})
            
    except Exception as e :
       
        return JsonResponse({"error": e}, status=400)
   
def local_register(request):
    form = LocalBankForm()
    return render(request=request, template_name="base/register.html", context={"register_form": form})


def foreign_register(request):
    myDict = dict(zip(request.POST.keys(), request.POST.values()))
    
    del myDict['csrfmiddlewaretoken']
    #print(**myDict)
    form = ForeignBank(**myDict)

    instance = form.save()
    print(myDict)
    # try:
    #     form = None
    #     if request.is_ajax and request.method == "POST":
    #          #print(request.POST['username'])
             
    #         myDict = dict(zip(request.POST.keys(), request.POST.values()))
    #         print(myDict)
    #         del myDict['csrfmiddlewaretoken']
    #         form = ForeignBank(**myDict)
    #         instance = form.save()
    #         return JsonResponse({"instance": "instance"})

    # except Exception as e:
        
    #     return JsonResponse({"error": e}, status=400)

def ForeignBank(request):
    form = ForiegnBankForm()
    context = {
        'reg_form':ForiegnBankForm
    }
    return render(request,'base/another_country_bank.html',context)



def login_page(request):
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LocalBank.objects.get(username=username)
        request.session['localbankid'] = user.id
        if username == user.username:
            messages.success(request, "Login successfull.")
            return redirect('login')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'base/login.html', context={"register_form": user})


def foreign_login_page(request):
    user = None
    if request.is_ajax and request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = ForeignBank.objects.get(username=username)
        print(user)
        request.session['localbankid'] = user.id
        if username == user.username:
            messages.success(request, "Login successfull.")
            return redirect('login')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'base/login.html', context={"register_form": user})


def add_client(request):
    clients = None
    localbankid = request.session.get('localbankid')
    localbankId = LocalBank.objects.get(id=localbankid)
    clients = ClientForm(request.POST or None)
    if request.method == "POST":
        if clients.is_valid():
            clients.save()
            clientid = UserProfile.objects.latest('id')
            data_dict = {
                'AccountNumber': request.POST['accountnumber'], 'BankID': localbankId, 'UserId': clientid}
            balance = UserBalance.objects.create(**data_dict)
            return redirect('addclient')

    return render(request, 'base/clients.html', context={"clients_form": clients})


def edit_client(request, pk):
    editform = None
    editform = EditClientForm(request.POST or None)
    if request.method == 'POST':
        if editform.is_valid():
            data = UserProfile.objects.filter(id=pk).update(name=request.POST.get(
                'name'), address=request.POST.get('address'), accountnumber=request.POST.get('AccountNumber'))
            obj = UserProfile.objects.get(id=pk)
            return redirect('edit_client', pk=obj.id)
            messages.success(request, "Client created  successfully.")
    return render(request, 'base/editclient.html',  context={"Editform": editform})


def make_transaction_request(request):
    localbankid = request.session.get('localbankid')
    localbank = LocalBank.objects.get(id=localbankid)
    if request.method == "POST":
        Tran_form = TransactionForm(request.POST)
        if Tran_form.is_valid():
            userid = request.POST['Name']
            name = UserProfile.objects.get(id=userid)
            tobank = ForeignBank.objects.get(
                pk=request.POST.get('toBank'))
            #routingnumber = str(tobank[0]['rountingnumber'])
            #toBank = str(tobank[0]['name'])
            data_dict = {
                'Accountnumber': request.POST['Accountnumber'], 'Name': name, 'FromBank': localbank,
                'toBank': ForeignBank.objects.get(), 'status': request.POST.get('status', False), 'amount': request.POST['amount'],
                'ForiegnBankrountingnumber': tobank}
            balance = Transaction.objects.create(**data_dict)
    form = TransactionForm()
    return render(request, 'base/transactionForm.html', context={"transaction_form": form})


def show_transanctions(request):
    context = None
    transaction_record = Transaction.objects.get()
    context = {
        'Transaction_data': transaction_record
    }

    return render(request, 'base/show_transactions.html', context)


def get_transaction_status(request):

    records = Transaction.objects.get()

    context = {
        'status': records.status
    }

    return render(request, 'base/show_transaction_status.html', context)


def confirm_pending_status(request, pk):
    if request.method == 'POST':
        status_confirmed = request.POST.get('confirm_status', False)
        Transaction.objects.filter(pk=pk).update(status=status_confirmed)
        messages.success(request, "Status Has Been  Confirmed successfully.")
    return render(request, 'base/confirmstatus.html')



def show_status_comp(request):
    context = None
    show_status = Transaction.objects.get()
    # return HttpResponse(show_status.status)
    if show_status.status == 'confirmed':
        return HttpResponse('sdfsdf')
        reverse('completed_transaction')
    else:
        return HttpResponse('Status Not confirmed Yet')
    # return render(request,'base/transactionDone.html')    




def get_all_users(request):
    users = UserProfile.objects.all()
    return HttpResponse(users)
