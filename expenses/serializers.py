from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    base_category = serializers.CharField(source="base_category.code", read_only=True)
    user_category = serializers.CharField(
        source="user_category.name", read_only=True
    )

    class Meta:
        model = Expense
        fields = (
            "id",
            "amount",
            "base_category",
            "user_category",
            "description",
            "expense_date",
            "created_at",
            "updated_at",
        )

class ExpenseCreateUpdateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    base_category_code = serializers.CharField()
    expense_date = serializers.DateField(required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    user_category_id = serializers.IntegerField(required=False, allow_null=True)
