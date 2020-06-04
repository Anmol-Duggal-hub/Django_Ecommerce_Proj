from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('wishlist', wishlist_page),
    path('checkout', checkout_page),
    path('product_details/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('cart', cart_page),
]