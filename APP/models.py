from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Expense(models.Model):
    amount = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=256)
    expense_date = models.DateField(default=now)
    description = models.TextField()

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-expense_date']


class Category(models.Model):
    name = models.CharField(max_length=256)
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name