from django.shortcuts import render


def signup(request):
    return render(request, 'authentication/sign_up.html')


def signin(request):
    return render(request, 'authentication/sign_in.html')
