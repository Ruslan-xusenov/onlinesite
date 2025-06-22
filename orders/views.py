from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem


@login_required
def order_create(request):
    cart = Cart(request)
    
    if len(cart) == 0:
        messages.warning(request, "❗ Savat bo‘sh. Buyurtma berish uchun mahsulot qo‘shing.")
        return redirect('cart:cart_detail')

    order = Order.objects.create(user=request.user)

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['product'].price,
            quantity=item['quantity']
        )

    cart.clear()

    messages.success(request, f"✅ Buyurtmangiz qabul qilindi! Buyurtma raqami: {order.id}")
    return render(request, 'orders/order_created.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})