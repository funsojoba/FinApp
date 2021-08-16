from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from APP.models import Expense


@login_required(login_url='auth/signin')
def index(request):
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = { 
        "expenses": expenses, 
        "page_obj": page_obj}
    return render(request, 'index.html', context)
