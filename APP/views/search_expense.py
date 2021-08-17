import json
from APP.models import Expense
from django.http import JsonResponse


def search_expense(request):
    search_str = json.loads(request.body).get('searchText')
    expense = Expense.objects.filter(
        amount__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            expense_date__istartswith=search_str, owner=request.user) | Expense.objects.filter(
                category__istartswith=search_str, owner=request.user) | Expense.objects.filter(
                    description__icontains=search_str, owner=request.user
                )
    data = expense.values()
    return JsonResponse(list(data), safe=False)
