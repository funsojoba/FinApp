from django.urls import path
from .views import user_preference


urlpatterns = [
    path('', user_preference, name='user_preference')
]
