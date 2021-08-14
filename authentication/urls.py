from django.contrib.auth.models import User
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views.sign_up import RegisterView, UsernameValidataionView, EmailValidationView, VerifyAccountView
from .views.sign_in import SignIn
from .views.sign_out import SignOutView

urlpatterns = [
    path('signup', RegisterView.as_view(), name="sign_up"),
    path('signin', SignIn.as_view(), name="sign_in"),
    path('sign_out', SignOutView.as_view(), name="sign_out"),
    path('verify-account/<uidb64>/<token>',
         VerifyAccountView.as_view(), name='verify_account'),
    path('validate-username', csrf_exempt(UsernameValidataionView.as_view()),
         name="validate_username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name="validate_email"),
]
