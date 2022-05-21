from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):

    product_name = serializers.SerializerMethodField(read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_name = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = History
        fields = [
            'id',
            'quantity',
            'price',
            'owner',
            'owner_name',
            'date',
            'product',
            'product_name'
        ]

    def get_product_name(self, obj):
        return obj.product.name

    def get_owner_name(self, obj):
        return obj.owner.username
