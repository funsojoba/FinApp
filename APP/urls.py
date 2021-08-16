from django.urls import path
from .views.index import index
from .views.add_expense import add_expense
from .views.edit_expense import edit_expense
from .views.delete_expense import delete_expense


urlpatterns = [
    path('', index, name="index"),
    path('add-expense', add_expense, name="add_expense"),
    path('edit-expense/<str:pk>', edit_expense, name="edit_expense"),
    path('delete-expense/<str:pk>', delete_expense, name="delete_expense"),
]
