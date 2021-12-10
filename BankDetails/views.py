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
from .serializers import TransactionSerializers
from rest_framework.decorators import api_view
from django.http import JsonResponse

import base64  # Module for password encryption



#  The above code is used to load all the packages from Django library or coustom files in this project 


#  The below codes are the various functions

# Create your views here.




# # # This Api function is called when we submit the Local bank Register form from the Local register page


def localbank_register_request(request):

    try:
        form = None
        if request.method == "POST":
            # print(request.POST['username'])

            myDict = dict(zip(request.POST.keys(), request.POST.values()))
            del myDict["csrfmiddlewaretoken"]
            password = myDict['password']. encode("utf-8")
            myDict['password'] = base64. b64encode(password)
            form = LocalBank(**myDict)
            instance = form.save()
            return JsonResponse({"instance": "instance"})

    except Exception as e:

        return JsonResponse({"error": e}, status=400)


# This is the used to load the Local Register Page


def local_register(request):
    form = LocalBankForm()
    return render(
        request=request,
        template_name="base/register.html",
        context={"register_form": form},
    )


# # This Api function is called when we submit the Foreign bank Register form from the Foreign register page
def foreign_register(request):

    try:
        form = None
        if request.method == "POST":
            print(request.POST["name"])
            myDict = dict(zip(request.POST.keys(), request.POST.values()))
            del myDict["csrfmiddlewaretoken"]
            print(myDict)
            password = myDict['password']. encode("utf-8")
            myDict['password'] = base64. b64encode(password)
            form = ForeignBank(**myDict)
            instance = form.save()
            return JsonResponse({"instance": "instance"})
        else:
            return JsonResponse({"instance": "Something went wrong"})
    except Exception as e:

        return JsonResponse({"error": e}, status=400)


# This is the used to load the Foriegn bank Register Page


def Foreign_bank_register(request):
    form = ForiegnBankForm()
    context = {"reg_form": ForiegnBankForm}
    return render(request, "base/another_country_bank.html", context)


# This is the used to load the Foriegn bank login Page


def login_local(request):
    user = LocalBankForm()
    return render(request, "base/login.html", context={"register_form": user})


# This Api function is called when we submit the Local bank Login form from the Local Login page


def login_page(request):
    user = None
    try:

        if request.method == "POST":

            username = request.POST["username"]
            password = request.POST["password"]
            password =password. encode("utf-8")
            password = base64. b64encode(password)
            user = LocalBank.objects.filter(
                username=username, password=password
            ).values("id", "username")

            username = request.POST["username"]
            password = request.POST["password"]
            user = LocalBank.objects.filter(
                username=username, password=password
            ).values("id", "username")
            print(len(user))
            if len(user) > 0:
                request.session["localbankid"] = user[0]["id"]
                request.session["Type"] = "Local"
            else:
                return JsonResponse({"instance": "Invalid Credentials"})
            if username == user[0]["username"]:
                messages.success(request, "Login successfull.")
                return JsonResponse({"instance": "user uploggeddated"})
        else:
            return JsonResponse({"instance": "Invalid Credentials"})
    except Exception as e:
        return JsonResponse({"error": e}, status=400)


# This Api function is called when we submit the Foreign bank Login form from the Foreign Login page


def foreign_login_page(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        password =password. encode("utf-8")
        password = base64. b64encode(password)
        user = ForeignBank.objects.filter(username=username, password=password).values(
            "id", "username"
        )
        if len(user) > 0:
            request.session["forienid"] = user[0]["id"]
            request.session["Type"] = "Foreign"
        else:
            return JsonResponse({"instance": "Invalid Credentials"})

        if username == user[0]["username"]:
            messages.success(request, "Login successfull.")
            return JsonResponse({"instance": "user uploggeddated"})
        else:
            messages.error(request, "Invalid Credentials")


# This function used to load the Foreign login page


def foreign_login(request):

    user = ForiegnBankForm()
    return render(request, "base/foreignlogin.html", context={"register_form": user})


# This function is used to load the Add client Form

def add_client_request(request):
    clients = ClientForm()
    return render(request, "base/clients.html", context={"clients_form": clients})

# This Api function is called when we submit the Add  Client form from the Add Client page

def add_client(request):

    clients = None
     
    localbankid = request.session.get("localbankid")    # Getting Local Bank id from session
    localbank = user = LocalBank.objects.get(id=localbankid) # Getting Local Bank instance or object 


    try:
        form = None
        if request.method == "POST":
            mydict = dict(zip(request.POST.keys(), request.POST.values()))
            del mydict["csrfmiddlewaretoken"]
            data_dict_user_profile = {
                "bankId": localbank,
                "address": request.POST["address"],
                "accountnumber": request.POST["accountnumber"],
                "name": request.POST["name"],
            }
            clients = UserProfile.objects.create(**data_dict_user_profile) # Create user profile table entry
            # instance = clients.save()
            clientid = UserProfile.objects.latest("id")

            data_dict = {
                "AccountNumber": request.POST["accountnumber"],
                "UserId": clientid,
            }
            instance = UserBalance.objects.create(**data_dict) # Create user balance table entry
            return JsonResponse({"instance": "instance"})

    except Exception as e:

        return JsonResponse({"error": e}, status=400)

#  This function used to load the show client page
def show_clients(request):
    localid = request.session.get("localbankid")

    clients_record = UserProfile.objects.filter(bankId=localid).values()
    context = {"clients_data": clients_record}
    return render(request, "base/showclients.html", context)


# This function used to load the Edit client Page

def edit_client_request(request, pk):
    editform = EditClientForm()

    return render(
        request, "base/editclient.html", context={"Editform": editform, "clientid": pk}
    )


# # This Api function is called when we submit the edit  Client form from the Edit Client page

def edit_client(request, pk):
    editform = None
    try:
        if request.method == "POST":  # Getting post request from Edit client page
            data = UserProfile.objects.filter(id=pk).update(
                name=request.POST["name"],
                address=request.POST["address"],
                accountnumber=request.POST["AccountNumber"],
            )
            instance = data
            return JsonResponse({"instance": "instance"})
    except Exception as e:

        return JsonResponse({"error": e}, status=400)


# This page is used to load the Transaction Form

def transaction(request):
    Tran_form = TransactionForm()
    return render(
        request, "base/transactionForm.html", context={"transaction_form": Tran_form}
    )

# This Api function is called when we submit the transaction form from the Create Transaction page

def make_transaction_request(request):
    # dt = datetime.datetime.now()
    date = time.strftime("%Y-%m-%d")
    # date = strftime('%Y%M%d')

    localbankid = request.session.get("localbankid")
    localbank = LocalBank.objects.get(id=localbankid) # Getting Local bank id From session
    print(localbankid)
    try:
        if request.method == "POST":
            mydict = dict(zip(request.POST.keys(), request.POST.values()))  # converting Queryset to python Dictionary
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

            Transaction.objects.create(**data_dict)   # submitting values to transaction page

            # Email sending

            print(settings.EMAIL_HOST_USER)
            port = settings.EMAIL_PORT
            smtp_server = settings.EMAIL_HOST
            sender_email = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            receiver_email = "saurav@codenomad.net"
            subject = "Incoming Transaction from " + localbank.name
            body = (
                "Please check incoming transaction of amount "
                + request.POST["amount"]
                + " with routing number "
                + tobank.rountingnumber
            )
            message = "Subject: {}\n\n{}".format(subject, body)
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

# This Api function is called when we show the clients transactions according to the status (Pending , Confirm , complete) 
# and in the else part we are retreiving transactions to show according to the filtering date

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
        data = ForeignBank.objects.get(
            id=str(transaction_pending[0]["ForiegnBankrountingnumber_id"])
        )

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

# This function is used to show the Foriegn Bank Transaction and in the else part we retreived the transaction for showing 
# according to the filteratio date


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

# This function is used to load the dates and stored into the session and I retreived the date matching
#  transaction from Database on the bais of Date  

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

# This function is used to confirm Pending status

def confirm_status(request, pk):
    # now = datetime.datetime.now()
    date = time.strftime("%Y-%m-%d")
    if request.method == "POST":
        mydict = dict(zip(request.POST.keys(), request.POST.values()))
        status_update = str(mydict["status"])
        instance = None
        if status_update == "confirmed":
            instance = Transaction.objects.filter(pk=pk).update(
                status=status_update, confirmdate=date
            )
        elif status_update == "complete":
            instance = Transaction.objects.filter(pk=pk).update(
                status=status_update, completeddate=date
            )
        return JsonResponse({"instance": "instance"})
        messages.success(request, "Status Has Been  Confirmed successfully.")

#  This function is used to complete pending status

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

# This function is used to logout the login user

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
