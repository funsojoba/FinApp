from APP.models import Expense
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required(login_url='auth/signin')
def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()
    messages.info(request, 'Expense deleted')
    return redirect('index')