from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):

    product_name = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = History
        fields = [
            'id',
            'quantity',
            'price',
            'owner',
            'date',
            'product',
            'product_name'
        ]

    def get_product_name(self, obj):
        return obj.product.name
