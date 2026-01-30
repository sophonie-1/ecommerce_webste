from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'product_name', 'price', 'quantity', 'total_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'full_name', 'email', 'total', 'status', 'paid', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    list_editable = ['status', 'paid']
    search_fields = ['order_number', 'user__username', 'full_name', 'email']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    list_per_page = 20
