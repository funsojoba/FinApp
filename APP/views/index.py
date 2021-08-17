from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from preference_app.models import UserPreference

from APP.models import Expense


@login_required(login_url='auth/signin')
def index(request):
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = 'USD'

    user_preference = UserPreference.objects.filter(user=request.user)
    if user_preference.exists():
        preference = UserPreference.objects.get(user=request.user)
        currency = preference.currency

    context = {
        "expenses": expenses,
        "page_obj": page_obj,
        "currency": currency}
    return render(request, 'expense/index.html', context)
