from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt

from .serializers import ShoppingListSerializer
from .models import ShoppingList


@api_view(["GET"])
def getAll(request):
    shopping_list = ShoppingList.objects.all()
    serializer = ShoppingListSerializer(shopping_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getById(request, id):
    shopping_list_element = ShoppingList.objects.get(id=id)
    if not shopping_list_element:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ShoppingListSerializer(shopping_list_element)
    return Response(serializer.data)


@api_view(['POST'])
def add(request):
    serializer = ShoppingListSerializer(data=request.data)
    if serializer.is_valid():
        shopping_list = serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        shopping_list = ShoppingList.objects.get(id=id)
        shopping_list.delete()
        return Response(id)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
