from django.urls import path
from .views import incomeView


urlpatterns = [
    path('', incomeView, name="income")
]
