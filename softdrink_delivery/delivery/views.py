from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product, Order, OrderItem

class ProductListView(ListView):
    model = Product
    template_name = 'delivery/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'delivery/product_detail.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'delivery/order_create.html'
    fields = ['customer_name', 'customer_email', 'customer_address']
    success_url = reverse_lazy('order_confirmation')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.total_amount = 0
        order.save()

        for item in self.request.POST.getlist('items'):
            product_id, quantity = item.split(',')
            product = Product.objects.get(id=product_id)
            quantity = int(quantity)  # Ensure quantity is an integer
            OrderItem.objects.create(order=order, product=product, quantity=quantity, unit=product.unit)
            order.total_amount += product.price * quantity

        order.save()
        return redirect('order_confirmation', pk=order.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context

class OrderConfirmationView(DetailView):
    model = Order
    template_name = 'delivery/order_confirmation.html'

class OrderListView(ListView):
    model = Order
    template_name = 'delivery/order_list.html'
    context_object_name = 'orders'
    ordering = ['-order_date']

