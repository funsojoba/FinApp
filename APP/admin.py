from django.contrib import admin
from .models import Expense, Category


admin.site.register((Expense, Category))