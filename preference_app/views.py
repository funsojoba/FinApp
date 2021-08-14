from django.shortcuts import render
import os
import json
from django.conf import settings


def user_preference(request):

    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    currencies = []

    with open(file_path) as json_file:
        file = json.load(json_file)

        for k, v in file.items():
            currencies.append({"key": k, "value": v})
    context = {
        "currencies": currencies
    }

    return render(request, 'preference/index.html', context)
