
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('transaction/<str:transaction_reference>/', views.TransactionDetailView.as_view(), name='transaction_view'),
    path('customer/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_view'),
    path('account/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_view'),
]
