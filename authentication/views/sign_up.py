import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User



class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/sign_up.html')

class UsernameValidataionView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({"username_error":"username should only contain alphanumeric characters"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error":"username already exist"}, status=400)


        return JsonResponse({"useername_valid":True})