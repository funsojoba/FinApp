import os
import json

from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

from .models import UserPreference


def user_preference(request):
    user_preference_exits = UserPreference.objects.filter(user=request.user).exists()
    user_preference_model = None
    
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    currencies = []

    with open(file_path) as json_file:
        file = json.load(json_file)

        for k, v in file.items():
            currencies.append({"key": k, "value": v})
    context = {
        "currencies": currencies
    }

    if request.method == 'GET':
        return render(request, 'preference/index.html', context)
    else:
        currency = request.POST['currency']
        if user_preference_exits:
            user_preference_model = UserPreference.objects.get(user=request.user)
            user_preference_model.currency = currency
            user_preference_model.save()
        else:
            user_pref = UserPreference.objects.create(
                user=request.user, currency=currency)
            user_pref.save()
        messages.success(request, 'Currency preference saved')
        return render(request, 'preference/index.html', {"currencies": currencies, 'user_preference': user_preference_model})
