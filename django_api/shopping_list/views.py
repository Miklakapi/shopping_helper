from rest_framework import authentication, generics, permissions
from .models import ShoppingList
from .serializers import ShoppingListSerializer


class ShoppingListRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticated]


class ShoppingListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    looup_field = 'pk'
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticated]
