from django.urls import path
from .views import ExpenseAnalyticsView, MonthlyExpenseAnalyticsView

urlpatterns = [
    path("summary/", ExpenseAnalyticsView.as_view(), name="expense-summary"),
    path("monthly/", MonthlyExpenseAnalyticsView.as_view(), name="monthly-summary"),    
]