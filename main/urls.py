from django.urls import path
from .views import short_url

urlpatterns = [
    path('short-url/',short_url,name='short-url'),
]
