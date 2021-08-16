from APP.models import Expense
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from APP.models import Category

@login_required(login_url='auth/signin')
def add_expense(request):

    categories = Category.objects.all()
    context={
        "categories":categories
    }

    if request.method == 'POST':
        amount = request.POST['amount']
        owner = request.user
        category = request.POST['category']
        expense_date = request.POST['expense_date']
        description = request.POST['description']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'add_expense.html', context)
        
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'add_expense.html', context)

        expense = Expense.objects.create(owner=owner, amount=amount, category=category, description=description, expense_date=expense_date )
        expense.save()
        messages.success(request, 'Expense added successfully')
        return redirect('index')
    return render(request, 'add_expense.html', context)
