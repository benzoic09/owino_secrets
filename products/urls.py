from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import shop, product_detail

urlpatterns = [
    path('', shop, name='shop'),
    path('<int:id>/', product_detail, name='product_detail'),
]

