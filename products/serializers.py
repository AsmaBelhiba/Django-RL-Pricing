#TODO add serializers for products
from rest_framework import serializers
from products.models import Product, ProductCategory, ProductPriceHistory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPriceHistory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    price_history = ProductPriceHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'