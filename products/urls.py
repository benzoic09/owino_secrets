from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import shop, product_detail, add_to_cart, cart_view, remove_from_cart

urlpatterns = [
    path('', shop, name='shop'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]