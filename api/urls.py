from django.urls import path
from api import api_views

urlpatterns = [
    path('send/', api_views.send_data, name='send'),
]
