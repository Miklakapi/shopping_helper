from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_name = serializers.SerializerMethodField(read_only=True)  
    
    class Meta:
        model = ShoppingList
        fields = [
            'id',
            'name', 
            'quantity', 
            'owner',
            'owner_name', 
            'date',
        ]

    def get_owner_name(self, obj):
        return obj.owner.username
