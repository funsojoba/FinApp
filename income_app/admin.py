from django.contrib import admin
from .models import Income, Source


admin.site.register((Income, Source))
