from django.contrib import admin
from .models import BaseCategory, UserCategory
# Register your models here.


@admin.register(BaseCategory)
class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active", "created_at")
    search_fields = ("code", "name")
    list_filter = ("is_active",)


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "base_category", "created_at")
    search_fields = ("name",)
    list_filter = ("base_category",)
