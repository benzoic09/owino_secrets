from django.shortcuts import render
from . models import Product, Category

# Create your views here.
def shop(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    return render(request, 'products/shop.html', {
        'products': products,
        'Category': categories,
    })

