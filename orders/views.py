from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from cart.views import get_or_create_cart


@login_required
def checkout(request):
    """Checkout page"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('shop:home')
    
    # Check stock availability
    for item in cart_items:
        if item.product.stock < item.quantity:
            messages.error(request, f'Sorry, {item.product.name} is out of stock.')
            return redirect('cart:cart')
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def process_checkout(request):
    """Process checkout and create order"""
    if request.method != 'POST':
        return redirect('orders:checkout')
    
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('shop:home')
    
    # Get form data
    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip_code')
    country = request.POST.get('country', 'USA')
    payment_method = request.POST.get('payment_method', 'Credit Card')
    
    # Validate required fields
    if not all([full_name, email, phone, address, city, state, zip_code]):
        messages.error(request, 'Please fill in all required fields.')
        return redirect('orders:checkout')
    
    # Check stock again
    for item in cart_items:
        if item.product.stock < item.quantity:
            messages.error(request, f'Sorry, {item.product.name} is out of stock.')
            return redirect('cart:cart')
    
    # Create order
    order = Order.objects.create(
        user=request.user,
        full_name=full_name,
        email=email,
        phone=phone,
        address=address,
        city=city,
        state=state,
        zip_code=zip_code,
        country=country,
        subtotal=cart.subtotal,
        total=cart.total,
        payment_method=payment_method,
        paid=True,  # Fake payment success
        status='processing'
    )
    
    # Create order items and update stock
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            product_name=item.product.name,
            price=item.product.final_price,
            quantity=item.quantity
        )
        # Update stock
        item.product.stock -= item.quantity
        item.product.save()
    
    # Clear cart
    cart.items.all().delete()
    
    messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
    return redirect('orders:order_success', order_id=order.id)


@login_required
def order_success(request, order_id):
    """Order success page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.select_related('product').all()
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_success.html', context)


@login_required
def order_history(request):
    """User's order history"""
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Order detail page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.select_related('product').all()
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_detail.html', context)
