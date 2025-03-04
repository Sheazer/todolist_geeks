from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return f"{self.title} - {self.amount} ({self.transaction_type})"
