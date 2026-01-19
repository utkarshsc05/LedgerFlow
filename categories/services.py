from django.core.exceptions import ValidationError
from .models import BaseCategory, UserCategory

def create_user_category(*, user, name, base_category_code):
    try:
        base_category = BaseCategory.objects.get(code=base_category_code, is_active=True)
    except BaseCategory.DoesNotExist:
        raise ValidationError("Invalid base category.")

    category, created = UserCategory.objects.get_or_create(
        user=user,
        name=name,
        defaults={"base_category": base_category},
    )

    if not created:
        raise ValidationError("Category already exists.")

    return category


def list_user_categories(user):
    return UserCategory.objects.filter(user=user).select_related("base_category")