from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Transanction_model,UserBalance

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transanction_model
        fields = "__all__"

class BalanceSerailizers(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = "__all__"

