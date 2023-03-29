from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
# todo Customers can be users with a given level of access
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(null=False, blank=False, unique=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


# Accounts linked to customers
class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    actual_balance = models.IntegerField( null=False)
    available_balance = models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.customer, self.pk)


# Transactions linked to a given account
class Transaction(models.Model):
    phone_number = models.CharField(max_length=20,null=False)

    transaction_reference = models.CharField(max_length=20, null=False, unique=True)
    transaction_code = models.CharField(max_length=20, null=False,unique=True)
    narration = models.CharField(max_length=20, null=True)
    amount = models.IntegerField(null=False)
