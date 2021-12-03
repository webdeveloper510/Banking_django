from django import http
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction, UserBalance, LocalBank, UserProfile, UserBalance, ForeignBank
from .serializers import TransactionSerializers, BalanceSerailizers
from django.contrib import messages
from django.contrib.auth import login
from django.db import connection
from .forms import LocalBankForm, ClientForm, EditClientForm, TransactionForm, StatusConfirmForm
from django.core.mail import EmailMultiAlternatives
from rest_framework.test import force_authenticate


# Create your views here.


@api_view(['GET'])
def api_transaction(request):
    transcation = Transaction.objects.all()
    serializer = TransactionSerializers(transcation, many=True)
    return Response(serializer.data)


def localbank_register_request(request):
    if request.method == "POST":
        form = LocalBankForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successfull.")
            return redirect("localbank_Register")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = LocalBankForm()
    return render(request=request, template_name="base/register.html", context={"register_form": form})


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


def add_client(request):
    localbankid = request.session.get('localbankid')
    if request.method == 'POST':
        clients = ClientForm(request.POST or None)
        if clients.is_valid():
            clients.save()
            clientid = clients.id
            request.session['client_id'] = clientid
            balance = UserBalance(
                AccountNumber=request.POST['accountnumber'], BankId=localbankid, UserID=clientid)
            balance.save()
            messages.success(request, "Client created  successfully.")
            return redirect('addclient')

        messages.error(request, "Something went wrong !!")
    clients = ClientForm()
    return render(request, 'base/add_client.html')


def edit_client(request, pk):
    context = None
    if request.method == 'POST':
        editform = EditClientForm(request.POST or None)
        if editform.is_valid():
            data = UserProfile.objects.filter(id=pk).update(editform)
            context = {
                'data': data,
            }
            messages.success(request, "Client created  successfully.")
    return render(request, 'base/editclient.html', context)

# def make_transaction_request(request, pk):

#     Foreinbankid = ForeignBank.objects.get(id=1)
#     localbankid = request.session.get('localbankid')
#     Localbankname = LocalBank.objects.get(id=localbankid)

#     if request.method == 'POST':
#         Post_Transaction = TransactionForm()
#         # view = TransactionForm.as_view()
#         if Post_Transaction.is_valid():
#             Post_Transaction.amount = 5000
#             Post_Transaction.save()
#             # subject, from_email, to = 'Status Pending Email', 'lucky@codenomad.net', 'amit@codenomad.net'
#             # html_content = '<strong>Please confirm Pending status</strong>'
#             # msg = EmailMultiAlternatives(
#             #     subject, from_email, [to])
#             # msg.send()
#             messages.success(request, "Transanction created  successfully.")
#             return HttpResponse('Done')
#             # response = view(request)
#             return redirect('base/transactionForm.html')

def make_transaction_request(request):

    if request.method == 'POST':
        # return HttpResponse(request.POST['amount'])
        form = TransactionForm(request.POST or None)
        if form.is_valid():
            form.amount = request.PSOT['amount']
            form.save()
    return render(request,'base/transactionForm.html')





def show_transanctions(request):
    context = None
    transaction_record = Transaction.objects.get()
    context = {
        'Transaction_data': transaction_record
    }

    # return render(request, 'Showtransactions.html', context)


def get_transaction_status(request):

    records = Transaction.objects.all()
    status = records.status

    context = {
        'transaction_status': status
    }
    return redirect('show_transaction', context)


def confirm_pending_status(request, pk):
    context = None
    if request.method == 'POST':
        status = StatusConfirmForm(request.POST['confirm_status'] or None)
        if status.is_valid():
            data = UserProfile.objects.filter(id=pk).update(status=status)
            context = {
                'status': data
            }
            messages.success(request, "Transanction Cofirmed")
            return redirect('confirm_status')
        messages.error(request, "Transanction Cofirmed Failed")
    status = StatusConfirmForm()
    return render(request, 'confirmstatus.html', context)
