from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Income, Source
from preference_app.models import UserPreference


def incomeView(request):
    income = Income.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    currency = 'USD'
    user_preference = UserPreference.objects.filter(user=request.user)
    if user_preference.exists():
        preference = UserPreference.objects.get(user=request.user)
        currency = preference.currency

    context = {
        "incomes": income,
        "page_obj": page_obj,
        "currency": currency,
    }
    return render(request, 'income/index.html', context)


def add_income(request):
    sources = Source.objects.all()

    context = {
        "sources": sources
    }

    if request.method == "POST":
        amount = request.POST['amount']
        source = request.POST['source']
        date = request.POST['income_date']
        description = request.POST['description']
        owner = request.user

        if not amount or not description:
            messages.error(request, 'both amount and description are required')
            return render(request, 'income/add_income.html', context)

        income = Income.objects.create(
            owner=owner, amount=amount, income_date=date, description=description, source=source)
        income.save()
        messages.success(request, 'Income created successfully')
        return render(request, 'income/add_income.html', context)
    return render(request, 'income/add_income.html', context)


def edit_income(request, pk):
    source = Source.objects.all()
    income = Income.objects.get(id=pk)
    context = {
        "sources": source,
        "income": income
    }

    if request.method == 'POST':
        amount = request.POST['amount']
        owner = request.user
        category = request.POST['category']
        income_date = request.POST['income_date']
        description = request.POST['description']

        if not amount or not description:
            messages.error(request, 'Both amount and description are required')
            return render(request, 'income/edit_income.html', context)

        income.amount = amount
        income.category = category
        income.income_date = income_date
        income.description = description
        income.owner = owner
        income.save()
        messages.success(request, 'Income updated successfully')
        return redirect('income')

    return render(request, 'income/edit_income.html', context)


def delete_income(request, pk):
    income = Income.objects.get(id=pk)
    income.delete()
    messages.info(request, 'Income Deleted')
    return redirect('income')