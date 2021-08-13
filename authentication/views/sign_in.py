import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages

from validate_email import validate_email


class SignIn(View):
    def get(self, request):
        return render(request, 'authentication/sign_in.html')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({"email_error": "email is not valid"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"email_error": "email already exist"}, status=400)

        return JsonResponse({"email_valid": True})


class UsernameValidataionView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({"username_error": "username should only contain alphanumeric characters"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error": "username already exist"}, status=400)

        return JsonResponse({"username_valid": True})
