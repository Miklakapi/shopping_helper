from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'category_name'
        ]

    def get_category_name(self, obj):
        return obj.category.name


class ProductBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
        ]
