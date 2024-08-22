from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def send_data(request):
    return Response({'value': 123})