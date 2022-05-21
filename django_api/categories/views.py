from rest_framework import generics
from .models import Categories
from .serializers import CategoriesSerializer


class CategoriesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    looup_field = 'pk'
