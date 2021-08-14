import json

from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site


from .utils import token_generator
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
                user.is_active = False

                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)
                domain = get_current_site(request).domain
                link = reverse("verify_account", kwargs={
                    "uidb64":uid,
                    "token":token
                })

                activate_url = 'http://'+domain+link

                email_subject = 'Account Activation'
                email_message = f"Hi {user.username}\n please follow the link below to activate your account \n {activate_url}"
                send_mail(
                    email_subject,
                    email_message,
                    'osnufwhale@gmail.com',
                    [email],
                    fail_silently=False,
                )
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


class VerifyAccountView(View):
    def get(self, request, uidb64, token ):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator(user, token):
                return redirect('sign_in'+'?message='+"User already exist")
                
            if user.is_active:
                return redirect('sign_in'+'?message='+'User already activated')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('sign_in')
        except:
            pass
        return redirect('sign_in')
    
