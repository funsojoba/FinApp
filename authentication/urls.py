from django.contrib.auth.models import User
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views.sign_up import RegisterView, UsernameValidataionView, EmailValidationView
from .views.sign_in import SignIn

urlpatterns = [
    path('signup', RegisterView.as_view(), name="sign_up"),
    path('signin', SignIn.as_view(), name="sign_in"),
    path('validate-username', csrf_exempt(UsernameValidataionView.as_view()), name="validate_username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name="validate_email"),
]
