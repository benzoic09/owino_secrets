from django.shortcuts import render, get_object_or_404
from . models import Product, Category

# Create your views here.
def shop(request):
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_available=True)

    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Category.objects.all()
    return render(request, 'products/shop.html', {
        'products': products,
        'Category': categories,
        'active_category': category_slug,
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})
