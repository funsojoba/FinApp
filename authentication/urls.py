from django.contrib.auth.models import User
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views.sign_up import RegisterView, UsernameValidataionView


urlpatterns = [
    path('signup', RegisterView.as_view(), name="sign_up"),
    path('validate-username', csrf_exempt(UsernameValidataionView.as_view()), name="validate-username")
]
