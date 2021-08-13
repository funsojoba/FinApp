import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

from validate_email import validate_email


class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/sign_up.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context ={
            "field_values": request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password must be more than 6 characters")
                    return render(request, 'authentication/sign_up.html', context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Account created successfully")
                return render(request, 'authentication/sign_up.html')
            messages.error(request, "email already exist")
            return render(request, 'authentication/sign_up.html', context)
        messages.error(request, "username already exist")
            
        return render(request, 'authentication/sign_up.html', context)

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
