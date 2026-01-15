from django.db import models
from django.conf import settings
from categories.models import BaseCategory, UserCategory
# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    base_category = models.ForeignKey(
        BaseCategory,
        on_delete=models.PROTECT,
        related_name="expenses"
    )
    user_category = models.ForeignKey(
        UserCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Expense amount with financial precision"
    )
    description = models.TextField(blank=True)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-expense_date", "-created_at"]

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.base_category.code})"
