from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type', 'category']
        widgets = {
            'transaction_type': forms.Select(choices=Transaction.TRANSACTION_TYPES),
        }