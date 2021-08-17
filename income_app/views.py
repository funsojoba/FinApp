from django.shortcuts import render


def incomeView(request):
    return render(request, 'income/index.html')
    