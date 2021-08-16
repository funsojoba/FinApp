from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from APP.models import Expense


@login_required(login_url='auth/signin')
def index(request):
    expenses = Expense.objects.filter(owner=request.user)

    context = {"expenses": expenses}
    return render(request, 'index.html', context)
