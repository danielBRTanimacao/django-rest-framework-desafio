from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def send_data(request):
    return Response({'value': request.POST.get('value')})

@api_view(['GET'])
def create_user(request):
    return Response({'response': 'funciona'})
