from django.urls import path
from .views import ExpenseAnalyticsView

urlpatterns = [
    path("summary/", ExpenseAnalyticsView.as_view(), name="expense-summary"),
]