from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer


# Create your views here.
class TransactionList(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class TransactionListView(ListView):
    model = Transaction
    template_name = 'finance/transaction_list.html'
    context_object_name = 'transactions'


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = 'finance/transaction_form.html'
    template_name = 'finance/transaction_form.html'
    success_url = reverse_lazy('transaction_list')
    