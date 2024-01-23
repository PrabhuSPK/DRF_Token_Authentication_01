from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializers


@api_view(['GET','POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def register(request):
    return Response({})

@api_view(['POST'])
def test_token(request):
    return Response({})