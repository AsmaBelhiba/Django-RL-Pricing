#TODO add serializers for products
from rest_framework import serializers
from products.models import Product, ProductCategory, ProductPriceHistory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def validate(self, attrs):
        """
        Custom validation to ensure that the category name is unique.
        """
        if ProductCategory.objects.filter(name=attrs.get('name')).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return attrs

class ProductPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPriceHistory
        fields = '__all__'

    def validate(self, attrs):
        """
        Custom validation to ensure that the price history entry is valid.
        """
        if attrs.get('price') <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return attrs

class ProductSerializer(serializers.ModelSerializer):
    price_history = ProductPriceHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
    
    def validate(self, attrs):
        """
        Custom validation to ensure that the product name is unique and prices are valid.
        """
        if Product.objects.filter(name=attrs.get('name')).exists():
            raise serializers.ValidationError("Product with this name already exists.")
        
        if attrs.get('base_price') <= 0 or attrs.get('current_price') <= 0 or attrs.get('cost_price') <= 0:
            raise serializers.ValidationError("Base price, current price, and cost price must be greater than zero.")
        
        if attrs.get('min_price') < 0 or attrs.get('max_price') < 0:
            raise serializers.ValidationError("Minimum and maximum prices must be non-negative.")
        
        return attrs