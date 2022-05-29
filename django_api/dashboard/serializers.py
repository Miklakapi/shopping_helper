from rest_framework import serializers


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


class SpendsByCategoryChartSerializer(serializers.Serializer):
    category_name = serializers.CharField()
    spends = serializers.FloatField()


class SpendsByProductChartSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    spends = serializers.FloatField()
