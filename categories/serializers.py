from rest_framework import serializers
from .models import UserCategory, BaseCategory

class UserCategorySerializer(serializers.ModelSerializer):
    base_category = serializers.CharField(source="base_category.code", read_only=True)

    class Meta:
        model = UserCategory
        fields = ("id", "name", "base_category", "created_at")


class UserCategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    base_category_code = serializers.CharField()


