import datetime
import calendar

from rest_framework import generics
from django.db.models import Sum
from rest_framework.response import Response
from django.urls import reverse
from django.db.models import F

from history.models import History
from .serializers import SpendsSerializer, SpendsByMonthChartSerializer, SpendsByMonthTableSerializer, SpendsByCategoryChartSerializer, SpendsByProductChartSerializer


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

        serializer = SpendsSerializer(data)
        return Response(serializer.data)


    def get_data_by_time(self, queryset, today_date, delta):
        if delta == -1:
            data = queryset.aggregate(sum=Sum('price'))
            if data['sum'] == None: 
                return 0
            return round(data['sum'], 2)
        data = None
        start_date = today_date - datetime.timedelta(days=delta)
        queryset = queryset.filter(date__range=(start_date, today_date))

        data = queryset.aggregate(sum=Sum('price'))
        if data['sum'] == None: 
            return 0
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


class SpendsByMonthTableListAPIVIew(generics.ListAPIView):
    queryset = History.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


    def list(self, request, year=datetime.datetime.now().year, *args, **kwargs):
        qs = self.get_queryset()
        result = []

        for x in range(1, 13):
            queryset = qs.filter(date__year=str(year), date__month=str(x))
            spends = queryset.aggregate(sum=Sum('price'))
            if spends['sum'] == None:
                spends['sum'] = 0
            result.append({"month": get_month_name(x), 'spends': spends['sum']})

        path = request.build_absolute_uri(reverse('month-table'))

        data = {
            'year': year, 
            'next': path + '/' + str(year + 1),
            'previous': path + '/' + str(year - 1),
            "results": result
        }

        serializer = SpendsByMonthTableSerializer(data)
        return Response(serializer.data)


class SpendsByCategoryChartListAPIVIew(generics.ListAPIView):
    queryset = History.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


    def list(self, *args, **kwargs):
        qs = self.get_queryset()

        qs = qs.values(category_name=F('product__category__name')).annotate(spends=Sum('price')).order_by('-spends')

        serializer = SpendsByCategoryChartSerializer(qs, many=True)
        return Response(serializer.data)


class SpendsByProductChartListAPIVIew(generics.ListAPIView):
    queryset = History.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


    def list(self, *args, **kwargs):
        qs = self.get_queryset()

        qs = qs.values(product_name=F('product__name')).annotate(spends=Sum('price')).order_by('-spends')

        serializer = SpendsByProductChartSerializer(qs, many=True)
        return Response(serializer.data)


def get_month_name(month):
    return calendar.month_name[month]
