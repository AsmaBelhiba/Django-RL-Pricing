from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    current_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.PositiveIntegerField(default=0)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    max_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    last_price_update = models.DateTimeField(auto_now=True)

    USE_RL_CHOICES = [
        ('RL', 'Reinforcement Learning Pricing'),
        ('STATIC', 'Traditional Static Pricing')
    ]
    pricing_strategy = models.CharField(
        max_length=10,
        choices=USE_RL_CHOICES,
        default='RL',
        help_text="RL = Reinforcement Learning Pricing, STATIC = Traditional Static Pricing"
    )
    last_strategy_change = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.base_price < 0 or self.current_price < 0 or self.cost_price < 0:
            raise ValidationError("Price fields cannot be negative.")
        if self.min_price < 0 or self.max_price < 0:
            raise ValidationError("Min and Max price cannot be negative.")
        if self.min_price > self.max_price:
            raise ValidationError("Min price cannot be greater than Max price.")
        if self.stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative.")
        
        now = timezone.now()
        if self.last_price_update > now:
            raise ValidationError("Last price update cannot be in the future.")

    def __str__(self):
        return self.name

class ProductPriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    change_percentage = models.FloatField(default=0.0) 
    
    units_sold = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['-timestamp']

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if self.change_percentage < -100 or self.change_percentage > 100:
            raise ValidationError("Change percentage must be between -100 and 100.")
        
        now = timezone.now()
        if self.timestamp > now:
            raise ValidationError("Timestamp cannot be in the future.")
    
    def __str__(self):
        return f"{self.product.name} - {self.price} at {self.timestamp}"
