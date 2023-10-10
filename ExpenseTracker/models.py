from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Custom validator to ensure amount is non-negative
def validate_positive_amount(value):
    if value < 0:
        raise ValidationError('Amount cannot be negative.')

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive_amount])
    date = models.DateField()

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ['-date']

    def __str__(self):
        return self.description
