from django.urls import path

from .views import AccountBooksAPIView, AccountBooksDetailAPIView, AccountBooksDetailRecoveryAPIView

app_name = "account_book"

urlpatterns = [
    path("api/v1/accountbooks", AccountBooksAPIView.as_view()),
    path("api/v1/accountbooks/<accountbook_id>", AccountBooksDetailAPIView.as_view()),
    path("api/v1/accountbooks/<accountbook_id>/recovery", AccountBooksDetailRecoveryAPIView.as_view()),
]
