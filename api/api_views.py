from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def create_user(request):
    return Response({'response': 'criando'})

@api_view(['GET'])
def login(request):
    return Response({'response': 'Entrando'})