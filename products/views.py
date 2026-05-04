from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Product, Category


def shop(request):
    category_slug = request.GET.get('category')

    products = Product.objects.filter(is_available=True)

    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Category.objects.annotate(
        product_count=Count('products')
    )

    return render(request, 'products/shop.html', {
        'products': products,
        'categories': categories,
        'active_category': category_slug,
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})



def add_to_cart(request, product_id):
    qty = int(request.POST.get('qty', 1))
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    request.session['cart'] = cart

    return redirect('cart')



def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        qty = cart[str(product.id)]
        subtotal = product.price * qty
        total += subtotal
        cart_items.append({
            'product': product,
            'qty': qty,
            'subtotal': subtotal
        })

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')
