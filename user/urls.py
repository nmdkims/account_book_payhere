from django.urls import path

from .views import LoginView, UserSignupApiView

urlpatterns = [
    path("signup", UserSignupApiView.as_view()),
    path("signin", LoginView.as_view()),
]
