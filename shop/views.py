from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Product, Cart, CartItem, Category

def count_cart_items(request):
    try:
        cart = Cart.objects.get(user=request.user)
        return cart.cartitem_set.aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0

def Mobile_view(request):
    category = get_object_or_404(Category, name='Apple Phones')
    products = Product.objects.filter(category=category)
    cart_items_count = count_cart_items(request)
    return render(request, 'Mobiles.html', {
        'category': category,
        'products': products,
        'cart_items_count': cart_items_count
    })

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart_items_count = count_cart_items(request)
    return render(request, 'product.html', {
        'products': products,
        'categories': categories,
        'cart_items_count': cart_items_count
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get the cart or create one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        # If the item already exists, just increase the quantity
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = cart.total
    cart_items_count = count_cart_items(request)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'cart_items_count': cart_items_count
    })