from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import expense_summary

# Create your views here.
class ExpenseAnalyticsView(APIView):
    
    def get(self, request):
        report = expense_summary(request.user)
        return Response(report)
    
