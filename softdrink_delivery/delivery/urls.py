from django.urls import path
from .views import ProductListView, ProductDetailView, OrderCreateView, OrderConfirmationView, OrderListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/confirmation/<int:pk>/', OrderConfirmationView.as_view(), name='order_confirmation'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]

