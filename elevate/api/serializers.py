from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: # here we specify the Attributes/Props
        model = Product
        fields = ['id', 'name', 'description', 'price']
        # fields = '__all__' 