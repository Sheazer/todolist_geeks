from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from django.db.models import Sum
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
import matplotlib.pyplot as plt
import io
import base64

from .models import Transaction
from .serializers import TransactionSerializer
from .forms import TransactionForm


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
    form_class = TransactionForm
    template_name = 'finance/transaction_form.html'
    success_url = reverse_lazy('transaction_list_view')


class FinanceDashboardView(View):
    def get(self, request):
        transactions = Transaction.objects.all()

        total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expense

        categories = transactions.values_list('category', flat=True).distinct()
        category_totals = [transactions.filter(category=cat).aggregate(Sum('amount'))['amount__sum'] for cat in categories]

        fig, ax = plt.subplots()
        ax.pie(category_totals, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        buffer.close()

        context = {
            'balance': balance,
            'total_income': total_income,
            'total_expense': total_expense,
            'chart': f"data:image/png;base64,{image_base64}"
        }

        return render(request, 'finance/dashboard.html', context)


