from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.models import Transaction, Account, Customer
from api.serializers import TransactionSerializer, AccountSerializer, CustomerSerializer


# Create your views here.
class TransactionDetailView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'transaction_reference'


class AccountDetailView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class CustomerDetailView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'
