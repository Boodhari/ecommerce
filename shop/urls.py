from django.urls import path
from .views import Product , product_list , view_cart, add_to_cart,Mobile_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('Mobile/', Mobile_view, name='mobile'),
]
