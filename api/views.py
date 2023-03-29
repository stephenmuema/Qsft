from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Transaction, Account, Customer
from api.serializers import TransactionSerializer, AccountSerializer, CustomerSerializer


@api_view(['GET', 'POST'])
def transactions_list(request):
    if request.method == 'GET':
        students = Transaction.objects.all()
        serializers = TransactionSerializer(students, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = TransactionSerializer(data=request.data)
        if serializers.is_valid():
            # modify accounts before saving
            serializers.save()
            phone_number = serializers.initial_data['phone_number']
            transaction_reference = serializers.initial_data['transaction_reference']
            transaction_code = serializers.initial_data['transaction_code']
            amount = serializers.initial_data['amount']
            account = Account.objects.get(customer__phone_number=phone_number)
            actual_balance = account.actual_balance + amount
            account.actual_balance = actual_balance
            account.available_balance = actual_balance
            account.save()
            available_balance = account.available_balance
            account_name = "{} {}".format(account.customer.first_name, account.customer.last_name)
            return Response({
                "transaction_reference": transaction_reference,
                "transaction_code": transaction_code,
                'amount': amount,
                "account_name": account_name,
                "phone_number": phone_number,
                "actual_balance": actual_balance,
                "available_balance": available_balance

            }, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


api_view(['GET'])


def transaction_details(request, transaction_reference):
    try:
        transaction = Transaction.objects.get(transaction_reference=transaction_reference)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = TransactionSerializer(Transaction)
        return Response(serializers.data)


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class ListCustomers(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.first_name + " " + user.last_name for user in Customer.objects.all()]
        return Response(usernames)
