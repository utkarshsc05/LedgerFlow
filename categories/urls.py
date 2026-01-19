from .views import UserCategoryListCreateView
from django.urls import path

urlpatterns = [
    path("user/", UserCategoryListCreateView.as_view(), name="user-categories"),
]