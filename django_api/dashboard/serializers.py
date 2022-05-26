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
