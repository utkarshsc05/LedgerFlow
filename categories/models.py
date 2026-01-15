from django.db import models

# Create your models here.
from django.db import models


class BaseCategory(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Stable system identifier, e.g. FOOD, TRANSPORT"
    )
    name = models.CharField(
        max_length=100,
        help_text="Human-readable category name"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Base Category"
        verbose_name_plural = "Base Categories"
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"
    


from django.conf import settings


class UserCategory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_categories"
    )
    base_category = models.ForeignKey(
        BaseCategory,
        on_delete=models.PROTECT,
        related_name="user_categories"
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "name")
        verbose_name = "User Category"
        verbose_name_plural = "User Categories"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.base_category.code})"
