from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Transaction, UserBalance


class TransactionSerializers(serializers.ModelSerializer):
    FromBank = serializers.StringRelatedField(many=False)
    toBank = serializers.StringRelatedField(many=False)

    class Meta:
        model = Transaction
        depth = 1
        fields = "__all__"


class BalanceSerailizers(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = "__all__"


