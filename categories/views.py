from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

from .serializers import UserCategorySerializer, UserCategoryCreateSerializer
from .services import create_user_category, list_user_categories
# Create your views here.

class UserCategoryListCreateView(APIView):

    def get(self, request):
        categories = list_user_categories(request.user)
        serializer = UserCategorySerializer(categories, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserCategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            category = create_user_category(
                user=request.user,
                **serializer.validated_data
            )
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(UserCategorySerializer(category).data, status=status.HTTP_201_CREATED)