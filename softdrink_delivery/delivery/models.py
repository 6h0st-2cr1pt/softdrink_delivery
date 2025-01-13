from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    UNIT_CHOICES = [
        ('CASE', 'Case'),
        ('PIECE', 'Piece'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default='PIECE')
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=5, choices=Product.UNIT_CHOICES, default='PIECE')

    def __str__(self):
        return f"{self.quantity} {self.get_unit_display()} of {self.product.name} in Order {self.order.id}"

