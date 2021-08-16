from APP.models import Expense
from APP.models import Category

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required



@login_required(login_url='auth/signin')
def edit_expense(request, pk):

    categories = Category.objects.all()
    expense = Expense.objects.get(id=pk)
    context = {
        "categories": categories,
        "expense":expense
    }

    if request.method == 'POST':
        amount = request.POST['amount']
        owner = request.user
        category = request.POST['category']
        expense_date = request.POST['expense_date']
        description = request.POST['description']

        if not amount or not description:
            messages.error(request, 'Both amount and description are required')
            return render(request, 'edit_expense.html', context)

        expense.amount = amount
        expense.category = category
        expense.expense_date = expense_date
        expense.description = description
        expense.owner = owner
        expense.save()
        messages.success(request, 'Expense updated successfully')
        return redirect('index')

    return render(request, 'edit_expense.html', context)
