from django.core.management.base import BaseCommand
from delivery.models import Supplier, Product
from django.core.files import File
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Adds sample products to the database'

    def handle(self, *args, **kwargs):
        supplier = Supplier.objects.create(
            name='Soft Drinks Inc.',
            contact_number='123-456-7890',
            email='info@softdrinksinc.com'
        )

        products = [
            {
                'name': 'Coca-Cola',
                'description': 'Classic cola flavor',
                'price': 1.99,
                'stock': 100,
                'unit': 'CASE',
                'image': 'coca-cola.jpg'
            },
            {
                'name': 'Pepsi',
                'description': 'Refreshing cola taste',
                'price': 1.89,
                'stock': 100,
                'unit': 'CASE',
                'image': 'pepsi.jpg'
            },
            {
                'name': 'Dr Pepper',
                'description': 'Unique blend of 23 flavors',
                'price': 2.09,
                'stock': 100,
                'unit': 'CASE',
                'image': 'dr-pepper.jpg'
            },
            {
                'name': 'Mountain Dew',
                'description': 'Citrus-flavored energy boost',
                'price': 1.99,
                'stock': 100,
                'unit': 'CASE',
                'image': 'mountain-dew.jpg'
            }
        ]

        for product_data in products:
            image_path = os.path.join(settings.MEDIA_ROOT, 'products', product_data['image'])
            product = Product.objects.create(
                supplier=supplier,
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                stock=product_data['stock'],
                unit=product_data['unit']
            )
            with open(image_path, 'rb') as image_file:
                product.image.save(product_data['image'], File(image_file), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully added sample products'))

