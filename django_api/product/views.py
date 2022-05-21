from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, ProductBaseSerializer


class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    looup_field = 'pk'


class ProductBaseListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductBaseSerializer
    looup_field = 'pk'
