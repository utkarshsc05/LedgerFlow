from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import expense_summary, monthly_expense_summary

# Create your views here.
class ExpenseAnalyticsView(APIView):
    
    def get(self, request):
        report = expense_summary(request.user)
        return Response(report)
    

class MonthlyExpenseAnalyticsView(APIView):

    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")

        if not year or not month:
            return Response(
                {"detail": "year and month query parameters are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return Response(
                {"detail": "year and month must be integers"},
                status=status.HTTP_400_BAD_REQUEST
            )

        report = monthly_expense_summary(
            request.user, year=year, month=month
        )
        return Response(report)
