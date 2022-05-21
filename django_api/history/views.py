from rest_framework import generics
from .models import History
from .serializers import HistorySerializer


class HistoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    looup_field = 'pk'
