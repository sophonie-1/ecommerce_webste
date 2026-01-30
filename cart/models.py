from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Cart(models.Model):
    """Shopping cart model"""
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id}"

    @property
    def total_items(self):
        """Calculate total number of items"""
        return sum(item.quantity for item in self.items.all())

    @property
    def subtotal(self):
        """Calculate subtotal"""
        return sum(item.total_price for item in self.items.all())

    @property
    def total(self):
        """Calculate total (for now same as subtotal, can add shipping later)"""
        return self.subtotal


class CartItem(models.Model):
    """Cart item model"""
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        """Calculate total price for this cart item"""
        return self.product.final_price * self.quantity
