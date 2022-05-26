import datetime
import calendar

from rest_framework import generics
from django.db.models import Sum
from rest_framework.response import Response

from history.models import History
from .serializers import SpendsSerializer, SpendsByMonthChartSerializer


class SpendsListAPIView(generics.ListAPIView):
    queryset = History.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


    def list(self, *args, **kwargs):
        qs = self.get_queryset()
        data = {}
        today_date = datetime.date.today()

        data['total'] = self.get_data_by_time(qs, today_date, -1)
        data['months'] = self.get_data_by_time(qs, today_date, 365)
        data['weeks'] = self.get_data_by_time(qs, today_date, 28)
        data['days'] = self.get_data_by_time(qs, today_date, 7)

        serializer = SpendsSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)


    def get_data_by_time(self, queryset, today_date, delta):
        if delta == -1:
            data = queryset.aggregate(sum=Sum('price'))
            return round(data['sum'], 2)
        data = None
        start_date = today_date - datetime.timedelta(days=delta)
        queryset = queryset.filter(date__range=(start_date, today_date))

        data = queryset.aggregate(sum=Sum('price'))
        return round(data['sum'], 2)


class SpendsByMonthChartListAPIVIew(generics.ListAPIView):
    queryset = History.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


    def list(self, *args, **kwargs):
        qs = self.get_queryset()

        today_date = datetime.datetime.now()
        year = today_date.year
        month = today_date.month

        data = []

        for x in range(12):
            queryset = qs.filter(date__year=str(year), date__month=str(month))
            spends = queryset.aggregate(sum=Sum('price'))
            data.append({"month": get_month_name(month), 'spends': spends['sum']})
            month -= 1
            if month == 0:
                month = 12
                year -= 1

        data.reverse()

        serializer = SpendsByMonthChartSerializer(data, many=True)
        return Response(serializer.data)


def get_month_name(month):
    return calendar.month_name[month]