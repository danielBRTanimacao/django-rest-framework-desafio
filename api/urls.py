from django.urls import path
from api import api_views

urlpatterns = [
    path('send/', api_views.send_data, name='send'),
    path('create/', api_views.create_user, name='create'),
    path('login/', api_views.login, name='login')
]
