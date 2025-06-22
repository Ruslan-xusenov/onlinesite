from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def category_products(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories, 'selected': category})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def location(request):
    return render(request, 'location.html')

def profile(request):
    return render(request, 'profile.html')

def likes_view(request):
    if request.user.is_authenticated:
        liked_products = Product.objects.filter(liked_by=request.user)
    else:
        liked_products = []

    return render(request, 'likes.html', {'liked_products': liked_products})

@login_required
def like_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user in product.liked_by.all():
        product.liked_by.remove(request.user)
    else:
        product.liked_by.add(request.user)

    return redirect('product_detail', pk=pk)