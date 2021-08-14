import json

from django.views import View
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth

from validate_email import validate_email


class SignIn(View):
    def get(self, request):
        return render(request, 'authentication/sign_in.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    messages.success(request, f'Welcome {user.username}')
                    return redirect('index')
                else:
                    messages.error(
                        request, 'Account is not active please check your mail')
                    return render(request, 'authentication/sign_in.html')
            messages.error(request, 'Invalid user credentials')
            return render(request, 'authentication/sign_in.html')
        messages.error(request, 'Please enter valid inputs')
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
