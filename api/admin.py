from django.contrib import admin

from api.models import Customer, Transaction, Account

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Account)