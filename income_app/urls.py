from django.urls import path
from .views import incomeView, add_income, edit_income, delete_income


urlpatterns = [
    path('', incomeView, name="income"),
    path('add-income', add_income, name="add_income"),
    path('edit-income/<str:pk>', edit_income, name="edit_income"),
    path('delete-income/<str:pk>', delete_income, name="delete_income"),

]
