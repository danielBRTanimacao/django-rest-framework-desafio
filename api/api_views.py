from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from api.serializers import UserSerializer

@api_view(['POST'])
def create_user(request, user_register: UserSerializer):
    user = UserSerializer(**user_register.user.dict())
    try:
        # user.full_clean()
        user.save(commit=False)
    except ValidationError as error:
        return {'error': error.message_dict}

    content = {
        'user': request.user.username,
    }
    return Response(content)

@api_view(['GET'])
def login(request):
    return Response({'response': 'Entrando'})