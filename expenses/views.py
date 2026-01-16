from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import Expense

# Create your views here.

from .serializers import (
    ExpenseSerializer,
    ExpenseCreateUpdateSerializer
)

from .services import(
    create_expense,
    update_expense,
    delete_expense,
    list_expenses,
)


class ExpenseListCreateView(APIView):

    def get(self, request):
        expenses = list_expenses(user=request.user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            expense = create_expense(
                user=request.user,
                **serializer.validated_data
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            ExpenseSerializer(expense).data,
            status=status.HTTP_201_CREATED
        )



class ExpenseDetailView(APIView):

    def put(self, request, pk):
        expense = get_object_or_404(
            Expense, pk=pk, user=request.user
        )

        serializer = ExpenseCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            expense = update_expense(
                expense=expense,
                user=request.user,
                **serializer.validated_data
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(ExpenseSerializer(expense).data)

    def delete(self, request, pk):
        expense = get_object_or_404(
            Expense, pk=pk, user=request.user
        )

        try:
            delete_expense(expense=expense, user=request.user)
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_403_FORBIDDEN
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
