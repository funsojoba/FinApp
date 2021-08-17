from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Income(models.Model):
    amount = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=256)
    income_date = models.DateField(default=now)
    description = models.TextField()

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-income_date']


class Source(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
