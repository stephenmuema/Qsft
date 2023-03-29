
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('transactions/', views.transactions_list, name='transaction_view'),
    # path('transaction/<srt:transaction_reference>/', views.transaction_details, name='transaction_detail_view'),
    # path('customers/', views.ListCustomers.as_view(), name='customer_view'),
    # path('account/<int:pk>/', views.AccountDetailView.as_view(), name='account_view'),
]
