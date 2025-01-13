from django.core.management.base import BaseCommand
from delivery.models import Product, Supplier

class Command(BaseCommand):
    help = 'Clears all products and suppliers from the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Supplier.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all products and suppliers'))

