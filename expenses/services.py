from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

from categories.models import BaseCategory, UserCategory
from .models import Expense


def create_expense(
    *,
    user,
    amount,
    base_category_code,
    expense_date=None,
    description="",
    user_category_id=None,
):
    """
    Create a new expense with strict validation.
    """

    if amount <= 0:
        raise ValidationError("Expense amount must be greater than zero.")

    try:
        base_category = BaseCategory.objects.get(
            code=base_category_code,
            is_active=True
        )
    except BaseCategory.DoesNotExist:
        raise ValidationError("Invalid or inactive base category.")

    user_category = None
    if user_category_id is not None:
        try:
            user_category = UserCategory.objects.get(
                id=user_category_id,
                user=user
            )
        except UserCategory.DoesNotExist:
            raise ValidationError("Invalid user category.")

    expense = Expense.objects.create(
        user=user,
        base_category=base_category,
        user_category=user_category,
        amount=Decimal(amount),
        description=description,
        expense_date=expense_date or timezone.now().date(),
    )

    return expense


def update_expense(
    *,
    expense,
    user,
    amount=None,
    base_category_code=None,
    expense_date=None,
    description=None,
    user_category_id=None,
):
    if expense.user != user:
        raise ValidationError("You do not have permission to modify this expense.")

    if amount is not None:
        if amount <= 0:
            raise ValidationError("Expense amount must be greater than zero.")
        expense.amount = Decimal(amount)

    if base_category_code is not None:
        try:
            expense.base_category = BaseCategory.objects.get(
                code=base_category_code,
                is_active=True
            )
        except BaseCategory.DoesNotExist:
            raise ValidationError("Invalid or inactive base category.")

    if user_category_id is not None:
        if user_category_id == "":
            expense.user_category = None
        else:
            try:
                expense.user_category = UserCategory.objects.get(
                    id=user_category_id,
                    user=user
                )
            except UserCategory.DoesNotExist:
                raise ValidationError("Invalid user category.")

    if description is not None:
        expense.description = description

    if expense_date is not None:
        expense.expense_date = expense_date

    expense.save()
    return expense


def delete_expense(*, expense, user):
    if expense.user != user:
        raise ValidationError("You do not have permission to delete this expense.")

    expense.delete()


def list_expenses(*, user, start_date=None, end_date=None, base_category_code=None):
    
    qs = Expense.objects.filter(user=user)

    if start_date:
        qs = qs.filter(expense_date__gte=start_date)

    if end_date:
        qs = qs.filter(expense_date__lte=end_date)

    if base_category_code:
        qs = qs.filter(base_category__code=base_category_code)

    return qs.select_related("base_category", "user_category")
