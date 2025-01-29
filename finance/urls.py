from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (TransactionList, TransactionListView, TransactionCreateView, FinanceDashboardView)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list_view'),
    path('transactions/', TransactionList.as_view(), name='transaction_list'),
    path('add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('dashboard/', FinanceDashboardView.as_view(), name='finance_dashboard'),
]
