from django.db.models import Sum
from rest_framework import serializers

from history.models import History


class SpendsSerializer(serializers.Serializer):
    total = serializers.FloatField()
    months = serializers.FloatField()
    weeks = serializers.FloatField()
    days = serializers.FloatField()


class SpendsByMonthChartSerializer(serializers.Serializer):
    month = serializers.CharField()
    spends = serializers.FloatField()

class SpendsByMonthTableSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    next = serializers.CharField()
    previous = serializers.CharField()
    results = serializers.ListField(child=SpendsByMonthChartSerializer())
