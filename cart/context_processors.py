from .models import Cart


def cart(request):
    """
    Context processor to make cart available in all templates
    """
    cart_obj = None
    cart_items_count = 0
    
    if request.user.is_authenticated:
        cart_obj = Cart.objects.filter(user=request.user).first()
    elif request.session.session_key:
        cart_obj = Cart.objects.filter(session_key=request.session.session_key).first()
    
    if cart_obj:
        cart_items_count = cart_obj.total_items
    
    return {
        'cart': cart_obj,
        'cart_items_count': cart_items_count,
    }
