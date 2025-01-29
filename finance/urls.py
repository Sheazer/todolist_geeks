from django.urls import path

from .views import TransactionList, TransactionListView, TransactionCreateView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
    path('add/', TransactionCreateView.as_view(), name='transaction_add'),
]
