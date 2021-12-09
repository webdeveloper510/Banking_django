from django import http
from django.core.exceptions import EmptyResultSet
from django.db.models.query import RawQuerySet
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import (
    Transaction,
    UserBalance,
    LocalBank,
    UserProfile,
    UserBalance,
    ForeignBank,
)
from .serializers import TransactionSerializers, BalanceSerailizers
from django.contrib import messages
from django.contrib.auth import login
from django.db import connection
from .forms import (
    LocalBankForm,
    ClientForm,
    EditClientForm,
    TransactionForm,
    StatusConfirmForm,
    ForiegnBankForm,
)
from django.core.mail import EmailMultiAlternatives
from rest_framework.test import force_authenticate
from django.shortcuts import get_object_or_404
from django.urls import reverse
from datetime import datetime
from django.utils import formats
import datetime
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import time
import smtplib
import ssl
# Create your views here.


def localbank_register_request(request):

    try:
        form = None
        if request.is_ajax and request.method == "POST":
            # print(request.POST['username'])

            myDict = dict(zip(request.POST.keys(), request.POST.values()))
            del myDict["csrfmiddlewaretoken"]
            form = LocalBank(**myDict)
            instance = form.save()
            return JsonResponse({"instance": "instance"})

    except Exception as e:

        return JsonResponse({"error": e}, status=400)


def local_register(request):
    form = LocalBankForm()
    return render(
        request=request,
        template_name="base/register.html",
        context={"register_form": form},
    )


def foreign_register(request):

    try:
        form = None
        if request.is_ajax and request.method == "POST":
            print(request.POST["name"])
            myDict = dict(zip(request.POST.keys(), request.POST.values()))
            del myDict["csrfmiddlewaretoken"]
            print(myDict)
            form = ForeignBank(**myDict)
            instance = form.save()
            return JsonResponse({"instance": "instance"})

    except Exception as e:

        return JsonResponse({"error": e}, status=400)


def Foreign_bank_register(request):
    form = ForiegnBankForm()
    context = {"reg_form": ForiegnBankForm}
    return render(request, "base/another_country_bank.html", context)


def login_local(request):
    user = LocalBankForm()
    return render(request, "base/login.html", context={"register_form": user})


def login_page(request):
    user = None
    if request.is_ajax and request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = LocalBank.objects.filter(username=username, password=password).values('id','username')
      
        
        request.session["localbankid"] = user[0]['id']
        request.session["Type"] = "Local"
        if username == user[0]['username']:
            messages.success(request, "Login successfull.")
            return JsonResponse({"instance": "user uploggeddated"})
        else:
            messages.error(request, "Invalid Credentials")


def foreign_login_page(request):
    if request.is_ajax and request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = ForeignBank.objects.get(username=username,password=password)
        
        
        request.session["forienid"] = user.id
        request.session["Type"] = "Foreign"
        if username == user.username:
            messages.success(request, "Login successfull.")
            return JsonResponse({"instance": "user uploggeddated"})
        else:
            messages.error(request, "Invalid Credentials")


def foreign_login(request):

    user = ForiegnBankForm()
    return render(request, "base/foreignlogin.html", context={"register_form": user})


def add_client_request(request):
    clients = ClientForm()
    return render(request, "base/clients.html", context={"clients_form": clients})


def add_client(request):

    clients = None

    localbankid = request.session.get("localbankid")
    localbank = user = LocalBank.objects.get(id=localbankid)
    localbankInstance = LocalBank.objects.filter(name=localbank)
    print(str(localbankInstance))

    try:
        form = None
        if request.is_ajax and request.method == "POST":
            mydict = dict(zip(request.POST.keys(), request.POST.values()))
            del mydict["csrfmiddlewaretoken"]
            data_dict_user_profile = {
                "bankId": localbank,
                "address": request.POST["address"],
                "accountnumber": request.POST["accountnumber"],
                "name": request.POST["name"],
            }
            # mydict["bankId"]  = localbankInstance,
            clients = UserProfile.objects.create(**data_dict_user_profile)
            # instance = clients.save()
            clientid = UserProfile.objects.latest("id")

            data_dict = {
                "AccountNumber": request.POST["accountnumber"],
                "UserId": clientid,
            }
            instance = UserBalance.objects.create(**data_dict)
            return JsonResponse({"instance": "instance"})

    except Exception as e:

        return JsonResponse({"error": e}, status=400)


def show_clients(request):
    localid = request.session.get("localbankid")

    clients_record = UserProfile.objects.filter(bankId=localid).values()
    context = {"clients_data": clients_record}
    return render(request, "base/showclients.html", context)


def edit_client_request(request, pk):
    editform = EditClientForm()

    return render(
        request, "base/editclient.html", context={"Editform": editform, "clientid": pk}
    )


def edit_client(request, pk):
    editform = None
    try:
        if request.is_ajax and request.method == "POST":
            data = UserProfile.objects.filter(id=pk).update(
                name=request.POST["name"],
                address=request.POST["address"],
                accountnumber=request.POST["AccountNumber"],
            )
            instance = data
            return JsonResponse({"instance": "instance"})
            messages.success(request, "Client updated  successfully.")
    except Exception as e:

        return JsonResponse({"error": e}, status=400)


def transaction(request):
    Tran_form = TransactionForm()
    return render(
        request, "base/transactionForm.html", context={"transaction_form": Tran_form}
    )


def make_transaction_request(request):
    # dt = datetime.datetime.now()
    date = time.strftime("%Y-%m-%d")
    # date = strftime('%Y%M%d')

    localbankid = request.session.get("localbankid")
    localbank = LocalBank.objects.get(id=localbankid)
    print(localbankid)
    try:
        if request.is_ajax and request.method == "POST":
            mydict = dict(zip(request.POST.keys(), request.POST.values()))
            del mydict["csrfmiddlewaretoken"]
            userid = request.POST["Name"]
            name = UserProfile.objects.get(id=userid)
            tobank = ForeignBank.objects.get(id=request.POST["toBank"])
            print(tobank)

            data_dict = {
                "Accountnumber": request.POST["Accountnumber"],
                "Name": name,
                "FromBank": localbank,
                "toBank": tobank,
                "amount": request.POST["amount"],
                "ForiegnBankrountingnumber": tobank,
                "date": str(date),
            }

            Transaction.objects.create(**data_dict)
            print(settings.EMAIL_HOST_USER)
            port = settings.EMAIL_PORT
            smtp_server = settings.EMAIL_HOST
            sender_email = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            receiver_email = 'saurav@codenomad.net'
            subject = 'Incoming Transaction from '+localbank.name
            body = 'Please check incoming transaction of amount '+request.POST["amount"] + ' with routing number '+tobank.rountingnumber
            message = 'Subject: {}\n\n{}'.format(subject, body)
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            return JsonResponse({"instance": "instance"})

    except Exception as e:
        return JsonResponse({"error": e}, status=400)


def show_transanctions(request):
    context = None
    dateInSession = request.session.get("datevalue")
    typeInSession = request.session.get("typeTab")
    LocalbankID = request.session.get("localbankid")

    print(dateInSession)
    print("typeInSession" + str(typeInSession))
    print("ForeignbankID" + str(LocalbankID))

    if dateInSession and typeInSession == "pending":
        transaction_pending = Transaction.objects.filter(
            status="pending", date=dateInSession
        ).values()
    else:
        transaction_pending = Transaction.objects.filter(
            FromBank_id=LocalbankID, status="pending"
        ).values()
    if dateInSession and typeInSession == "confirm":
        transaction_confirm = Transaction.objects.filter(
            status="confirmed", confirmdate=dateInSession
        ).values()
    else:
        transaction_confirm = Transaction.objects.filter(
            FromBank_id=LocalbankID, status="confirmed"
        ).values()
    if dateInSession and typeInSession == "complete":
        transaction_completed = Transaction.objects.filter(
            status="complete", completeddate=dateInSession
        ).values()
    else:
        transaction_completed = Transaction.objects.filter(
            FromBank_id=LocalbankID, status="complete"
        ).values()
    request.session["datevalue"] = None
    context = {
        "Transaction_pending": transaction_pending,
        "Transaction_confirm": transaction_confirm,
        "Transaction_completed": transaction_completed,
    }

    return render(request, "base/show_transactions.html", context)


def show_foreign_transaction(request):

    context = None
    dateInSession = request.session.get("datevalue")
    typeInSession = request.session.get("typeTab")
    ForeignbankID = request.session.get("forienid")

    print(dateInSession)
    print("typeInSession" + str(typeInSession))
    print("ForeignbankID" + str(ForeignbankID))

    if dateInSession and typeInSession == "pending":
        transaction_pending = Transaction.objects.filter(
            status="pending", date=dateInSession
        ).values()
    else:
        transaction_pending = Transaction.objects.filter(
            toBank_id=ForeignbankID, status="pending"
        ).values()
    if dateInSession and typeInSession == "confirm":
        transaction_confirm = Transaction.objects.filter(
            status="confirmed", confirmdate=dateInSession
        ).values()
    else:
        transaction_confirm = Transaction.objects.filter(
            toBank_id=ForeignbankID, status="confirmed"
        ).values()
    if dateInSession and typeInSession == "complete":
        transaction_completed = Transaction.objects.filter(
            status="complete", completeddate=dateInSession
        ).values()
    else:
        transaction_completed = Transaction.objects.filter(
            toBank_id=ForeignbankID, status="complete"
        ).values()
    request.session["datevalue"] = None
    context = {
        "Transaction_pending": transaction_pending,
        "Transaction_confirm": transaction_confirm,
        "Transaction_completed": transaction_completed,
    }
    return render(request, "base/foreign_transaction.html", context)


def date_request(request):
    date = dict(zip(request.POST.keys(), request.POST.values()))
    print(date)
    # del date["csrfmiddlewaretoken"]
    print(date)
    request.session["datevalue"] = date["date"]
    request.session["typeTab"] = date["type"]
    return redirect("show_transaction")


def get_transaction_status(request):

    records = Transaction.objects.all().values()
    context = {"status": records}

    return render(request, "base/show_transaction_status.html", context)


def confirm_status(request, pk):
    # now = datetime.datetime.now()
    date = time.strftime("%Y-%m-%d")
    if request.is_ajax and request.method == "POST":
        mydict = dict(zip(request.POST.keys(), request.POST.values()))
        status_update = str(mydict["status"])
        instance = None
        if status_update == "confirmed":
            instance = Transaction.objects.filter(pk=pk).update(
                status=status_update, confirmdate=date
            )
        elif status_update == "completed":
            instance = Transaction.objects.filter(pk=pk).update(
                status=status_update, completeddate=date
            )
        return JsonResponse({"instance": "instance"})
        messages.success(request, "Status Has Been  Confirmed successfully.")


def show_status_comp(request):
    context = None
    show_status = Transaction.objects.get()
    # return HttpResponse(show_status.status)
    if show_status.status == "confirmed":
        return HttpResponse("sdfsdf")
        reverse("completed_transaction")
    else:
        return HttpResponse("Status Not confirmed Yet")
    # return render(request,'base/transactionDone.html')


def get_all_users(request):
    users = UserProfile.objects.all()
    return HttpResponse(users)


def index_request(request):
    return render(request, "base/index.html")


def about_request(request):
    return render(request, "base/about.html")


def services_request(request):
    return render(request, "base/services.html")


def contact_request(request):
    return render(request, "base/contacts.html")


def header_request(request):
    print("hgere")
    LocalbankID = request.session.get("localbankid")
    ForeignbankID = request.session.get("forienid")
    Type = request.session.get("Type")
    print(Type)
    return render(request, "base/header.html", LocalbankID, ForeignbankID, Type)


def logout_request(request):
    request.session["Type"] = ""
    request.session["LocalbankID"] = ""
    request.session["ForeignbankID"] = ""
    return redirect("")


def footer_request(request):
    return render(request, "base/footer.html")


def single_request(request):
    return render(request, "base/single.html")


def blog_request(request):
    return render(request, "base/blog.html")
