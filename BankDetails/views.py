from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transanction_model,UserBalance
from .serializers import TransactionSerializers,BalanceSerailizers
# Create your views here.

@api_view(['GET'])
def api_transaction(request):
    transcation = Transanction_model.objects.all()
    serializer = TransactionSerializers(transcation,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_balance(request):
    balance = UserBalance.objects.all()
    serializers = BalanceSerailizers(balance,many=True)
    return Response(serializers.data)