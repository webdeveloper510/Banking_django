from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Transanction,UserBalance

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transanction
        fields = "__all__"

class BalanceSerailizers(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = "__all__"

