from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('cart', OrderSummaryView.as_view(), name='cart'),
    path('wishlist', wishlist_page),
    path('checkout', Checkout_Page.as_view(), name='checkout'),
    path('product_details/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-item-from-cart/<slug>/', add_single_item_from_cart, name='add-single-item-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart')
]
