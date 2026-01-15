from django.contrib import admin
from .models import Expense
# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "amount",
        "base_category",
        "user_category",
        "expense_date",
        "created_at",
    )
    list_filter = ("base_category", "expense_date")
    search_fields = ("description",)
