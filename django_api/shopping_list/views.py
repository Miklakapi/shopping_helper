from rest_framework import generics

from .models import ShoppingList
from .serializers import ShoppingListSerializer


class ShoppingListRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    looup_field = 'pk'
